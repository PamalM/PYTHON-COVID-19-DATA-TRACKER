import json
import requests
from datetime import datetime, timedelta
import fileManager

#Path for countries.json
countriesjsonpath = "JSON/countries.json"

#region Helper Methods
#Template for an empty case dictionary
def __blankCaseDict():
    return {"Confirmed": 0,"Deaths": 0,"Recovered": 0,"Active": 0}

#Converts string format YYYY-MM-DD to a datetime object
def __convertStringDatetime(string):
    append = f'{string} 00:00:00.000000'
    return datetime.strptime(append,'%Y-%m-%d %H:%M:%S.%f')

#Finds the index of an object within a given list
def __indexOfValueInList(string, searchobject, searchlist):
    index = 0
    for val in searchlist:
        if val[string] == searchobject: break
        else: index += 1
    return index

#Assigns all case parameters from a given dictionary to a blank case dictionary and returns it
def __assignCases(value):
    cases = __blankCaseDict()
    cases["Confirmed"] = value["Confirmed"]
    cases["Deaths"] = value["Deaths"]
    cases["Recovered"] = value["Recovered"]
    cases["Active"] = value["Active"]
    return cases

#Converts string to proper json file naming convention (lowercase, spaces replaced with '-')
def __jsonnameConversion(string):
    return string.lower().replace(" ","-")

def __getCountryDir(country):
    return f"JSON/Countries/{country}"

def __getCountryJson(country):
    jsonname = __jsonnameConversion(country)
    return f"{__getCountryDir(country)}/{jsonname}.json"

def __getProvinceDir(country, province):
    return f"{__getCountryDir(country)}/{province}"

def __getProvinceJson(country, province):
    jsonname = __jsonnameConversion(province)
    return f"{__getProvinceDir(country, province)}/{jsonname}.json"

def __getDateDir(country, province, date):
    return f"{__getProvinceDir(country, province)}/{date}"

def __getDateJson(country, province, date):
    return f"{__getDateDir(country, province, date)}/{date}.json"
#endregion Helper Methods

#region Parsing Methods
#Reformats the returned json and organizes information into subdirectories
def __parseJson(data, slug):
    #Get country name
    country = data[0]["Country"]

    #Get list of provinces
    provinces = []
    [provinces.append(value["Province"]) for value in data if(value["Province"] not in provinces)]

    #Find the earliest date listed
    earliestdate = datetime.today()
    for value in data:
        tempdate = __convertStringDatetime(value["Date"][0:10])
        if(tempdate < earliestdate):
            earliestdate = tempdate

    #Creates a list of all dates from the earliest date to today
    dates = []
    while str(earliestdate)[0:10] != str(datetime.today()+timedelta(days=1))[0:10]:
        dates.append(str(earliestdate)[0:10])
        earliestdate += timedelta(days=1)

    #Get list of dates for each province and parse the dates
    for province in provinces:
        __parseDates(country, province, dates, data)

    #parse the country and provinces
    __parseProvinces(country, provinces, data)
    __parseCountry(country, data, slug)

def __parseCountry(country,data,slug):
    #Check if countries json file exists, if not, create it
    fileManager.jsonPreset(countriesjsonpath,"countries")

    #Get index of country in json array
    countrieslist = fileManager.readList(countriesjsonpath,"countries")
    index = __indexOfValueInList("country", country, countrieslist)

    #Get the number of country directories that ar in the Countries folder
    provincecount = fileManager.directoryCount(__getCountryDir(country))

    #Get the total count of case values across all provinces
    cases = []
    #Used to only create a new dictionary for each country and append it to the cases list once
    init = False
    for i in range(provincecount):
        try:
            #Retrieve province info
            province = fileManager.readJson(__getCountryJson(country))["provinces"][i]
            provincename = province["province"]

            #Get the number of date directories in the current provinces directory
            datecount = fileManager.directoryCount(__getProvinceDir(country, provincename))

            for j in range(datecount):

                #Retrieve date info
                datesfile = fileManager.readJson(__getProvinceJson(country, provincename))["dates"][j]
                date = datesfile["date"]

                #Attempt to add the current provinces case counts for each date to the cases list
                try:
                    #If the cases dictionaries haven't been created yet, create and append them
                    if not init:
                        newdict = {"date":date,"cases":__blankCaseDict()}
                        cases.append(newdict)

                    #If the directory contains a total count of cases across all provinces
                    #use that information
                    if provincename == "All Provinces":
                        cases[j]["cases"] = datesfile["cases"]
                        continue
                    #Sum up the cases from all the listed provinces
                    # print(province["cases"])
                    cases[j]["cases"]["Confirmed"] += datesfile["cases"]["Confirmed"]
                    cases[j]["cases"]["Deaths"] += datesfile["cases"]["Deaths"]
                    cases[j]["cases"]["Recovered"] += datesfile["cases"]["Recovered"]
                    cases[j]["cases"]["Active"] += datesfile["cases"]["Active"]

                except KeyError:
                    continue

            init = True

        except IndexError:
            continue

    #Create the json file for the given country
    path = __getCountryJson(country)
    newinfodict = {"country":country,"slug":slug,"file":path,"dates":cases}

    if(index < len(countrieslist)): countrieslist[index] = newinfodict
    else: countrieslist.append(newinfodict)

    #Rewrite the json file
    fileManager.writeList(countriesjsonpath,"countries",countrieslist)

def __parseProvinces(country,provinces,data):
    for province in provinces:
        if province == "": province = "All Provinces"

        #Get the country's json path
        countryjsonpath = __getCountryJson(country)

        #Check if provinces json file exists, if not, create it
        fileManager.jsonPreset(countryjsonpath,"provinces")

        #Get index of province in json array
        provinceslist = fileManager.readList(countryjsonpath,"provinces")
        index = __indexOfValueInList("province", province, provinceslist)

        #Get the most recent number of cases
        provincedir = __getProvinceDir(country, province)
        cases = __blankCaseDict()
        datecount = fileManager.directoryCount(provincedir)

        #Update the province's cases dict to the most recent dates values
        for i in range(datecount):
            currDate = str(datetime.today() - timedelta(days=i))[0:10]
            datepath = f"{provincedir}/{currDate}/{currDate}.json"
            if fileManager.exists(datepath):
                recent = fileManager.readJson(datepath)
                cases = recent
                break

        #Get the province's json path
        provincejson = __getProvinceJson(country, province)
        #Create the province's new information dictionary with the updated case counts
        newinfodict = {"province":province,"file":provincejson,"cases":cases}

        #Replace the province's old values if it already exists within the list,
        #otherwise append the new province's information
        if(index < len(provinceslist)): provinceslist[index] = newinfodict
        else: provinceslist.append(newinfodict)

        #Rewrite the country's json file
        fileManager.writeList(countryjsonpath,"provinces",provinceslist)

def __parseDates(country,province,dates,data):
    #Used to check the data file with the original name of province
    checkprovince = province
    if province == "": province = "All Provinces"

    #Keep track of the current position in the dates list to be able to reference the previous date
    index = 0
    for date in dates:
        #Check if date's directory exists, if not, create it
        fileManager.mkexistsdir(__getDateDir(country, province, date))

        #Get the province's json path
        provincejson = __getProvinceJson(country, province)

        #Check if dates json file exists, if not, create it
        fileManager.jsonPreset(provincejson,"dates")

        #Load existing dates.json file
        dateslist = fileManager.readList(provincejson,"dates")

        #Get the date's json path
        path = __getDateJson(country, province, date)

        #If the date doesn't exist in the directory create it, otherwise skip it as date information
        #doesn't need to be rewritten
        if not fileManager.exists(path):
            #Keep track of whether the date was found in the retrieved API information
            foundfromapi = False

            cases = __blankCaseDict()
            #Check all the dates listed from the API json
            for value in data:
                #If the value of the current date and province matches the API data assign the case counts
                if(value["Date"].startswith(date) and value["Province"] == checkprovince):
                    cases = __assignCases(value)
                    foundfromapi = True
                    break
            #If the case info couldn't be found in the API json, use the previous dates values instead
            if(not foundfromapi):
                try:
                    #Get the previous date json
                    prevdate = fileManager.readJson(__getDateJson(country, province, dates[index-1]))
                    cases = __assignCases(prevdate)
                except FileNotFoundError:
                    pass

            #Write the case information to the date's json file
            fileManager.writeJson(path,cases)

            #Create the new date's information dictionary and append it to the list of dates
            newinfodict = {"date":date,"file":path,"cases":cases}
            dateslist.append(newinfodict)

        #Rewrite the province's json file
        fileManager.writeList(provincejson,"dates",dateslist)
        index += 1

#endregion Parsing Methods

#region Data Retrival Methods
#Returns a dictionary with Covid-19 Case counts
def getCases(slug, attempts=3, date=str(datetime.today())[0:10]):

    #Default cases count to return if values cannot be found
    nocases = __blankCaseDict()

    try:
        #Searches through the countries json file to pick the appropriate country's case numbers
        if(fileManager.exists(countriesjsonpath)):
            countries = fileManager.readJson(countriesjsonpath)
            targetcountry = [country for country in countries["countries"] if country["slug"] == slug]
            for i in range(len(targetcountry[0]["dates"])):
                cases = [country["dates"][i]["cases"] for country in countries["countries"] if country["slug"] == slug and country["dates"][i]["date"] == date]
                #Provided the country exists in the database the country's case counts will be returned
                if cases != []: return cases[0]
    except IndexError:
        pass

    #If the country's case counts can not be found the following will be executed

    #Fetch most recent data from Covid19 API and update the JSON directory
    print("Fetching data from API...")
    response = requests.get("https://api.covid19api.com/live/country/" + slug)
    __parseJson(response.json(), slug)

    #Could not find data after x attempts, returns an invalid case dictionary
    if(attempts == 0): return nocases
    #Otherwise try again now that data has been retrieved
    else: return getCases(slug, attempts-1, date)

def getCasesList(slug, attempts=3, startdate="2020-04-13", enddate=str(datetime.today())[0:10]):
    caselist = []
    #Earliest date provided by the API
    mindate = __convertStringDatetime("2020-04-13")

    currentdate = __convertStringDatetime(startdate)
    lastdate = __convertStringDatetime(enddate)

    if currentdate < mindate:
        currentdate = mindate

    while str(currentdate)[0:10] != str(lastdate)[0:10]:
        caselist.append({"date":str(currentdate)[0:10], "cases":getCases(slug, 3, str(currentdate)[0:10])})
        currentdate += timedelta(days=1)

    return caselist
#endregion Data Retrieval Methods