import json
import requests
from datetime import datetime, timedelta
import fileManager

#Path for countries.json
countriesjsonpath = "JSON/countries.json"
continentsjsonpath = "JSON/continents.json"
worldjsonpath = "JSON/world.json"

#region Converters
slugtoname = {
    "canada":"Canada",
    "italy":"Italy",
    "spain":"Spain",
    "united-states":"United States of America",
    "united-kingdom":"United Kingdom",
    "france":"France"
}

nametoslug = {
    "Canada":"canada",
    "Italy":"italy",
    "Spain":"spain",
    "United States of America":"united-states",
    "United Kingdom":"united-kingdom",
    "France":"france"
}

slugtoalpha2 = {
    "canada":"CA",
    "italy":"IT",
    "spain":"ES",
    "united-states":"US",
    "united-kingdom":"GB",
    "france":"FR"
}

alpha2toslug = {
    "CA":"canada",
    "IT":"italy",
    "ES":"spain",
    "US":"united-states",
    "GB":"united-kingdom",
    "FR":"france"
}

alpha2toname = {
    "CA":"Canada",
    "IT":"Italy",
    "ES":"Spain",
    "US":"United States of America",
    "GB":"United Kingdom",
    "FR":"France"
}

nametoalpha2 = {
    "Canada":"CA",
    "Italy":"IT",
    "Spain":"ES",
    "United States of America":"US",
    "United Kingdom":"GB",
    "France":"FR"
}
#endregion Converters

#region Helper Methods
#Template for an empty case dictionary
def __blankCaseDict():
    return {"Confirmed": 0,"Deaths": 0,"Recovered": 0,"Active": 0}

def __errorCaseDict():
    return {"Confirmed": -1,"Deaths": -1,"Recovered": -1,"Active": -1}

#Converts string format YYYY-MM-DD to a datetime object
def __convertStringDatetime(string):
    append = f'{string} 00:00:00.000000'
    return datetime.strptime(append,'%Y-%m-%d %H:%M:%S.%f')

def __convertDatetimeString(datetime):
    return str(datetime)[0:10]

def __convertSlashDate(date):
    parts = date.split("/")

    if(len(parts[0]) == 1): returndate = f"20{parts[2]}-0{parts[0]}-{parts[1]}"
    else: returndate = f"20{parts[2]}-{parts[0]}-{parts[1]}"

    return returndate

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
def __storeAsJson(*data, worldwide=False, continents=False, country=False, countryslug="canada", provinces=False):

    if(worldwide):
        __storeAsJsonWorldwide(data)
    elif(continents):
        __storeAsJsonContinents(data)
    elif(country):
        __storeAsJsonCountry(data, countryslug)
    elif(provinces):
        __storeAsJsonCountryProvinces(data)
    else:
        print("No parameters selected...")

def __storeAsJsonWorldwide(data):
    __parseWorld(data)

def __storeAsJsonContinents(data):
    __parseContinents(data)

def __storeAsJsonCountry(data, countryslug):
    countryname = slugtoname[countryslug]
    __parseCountry(countryname, countryslug, data)

def __storeAsJsonCountryProvinces(data):
    #fix for weird python thing wrapping data in another list
    data = data[0]

    #Get country name
    countryname = data[0]["Country"]

    #Get list of provinces
    provinces = []
    [provinces.append(value["Province"]) for value in data if(value["Province"] not in provinces)]

    #Find the earliest date listed
    earliestdate = datetime.today()
    for value in data:
        tempdate = __convertStringDatetime(__convertDatetimeString(value["Date"]))
        if(tempdate < earliestdate):
            earliestdate = tempdate

    #Creates a list of all dates from the earliest date to today
    dates = []
    while __convertDatetimeString(earliestdate) != __convertDatetimeString(datetime.today()+timedelta(days=1)):
        dates.append(__convertDatetimeString(earliestdate))
        earliestdate += timedelta(days=1)

    #Get list of dates for each province and parse the dates
    for province in provinces:
        __parseDates(countryname, province, dates, data)

    #parse the country and provinces
    __parseProvinces(countryname, provinces)

def __parseWorld(data):
    pass

def __parseContinents(data):
    # fileManager.mkexistsdir("JSON")
    # #Check if countries json file exists, if not, create it
    # fileManager.jsonPreset(continentsjsonpath,"continents")

    # dates = []
    pass

def __parseCountry(country, slug, data):
    fileManager.mkexistsdir("JSON")
    #Check if countries json file exists, if not, create it
    fileManager.jsonPreset(countriesjsonpath,"countries")

    #Get index of country in json array
    countrieslist = fileManager.readList(countriesjsonpath,"countries")
    index = __indexOfValueInList("country", country, countrieslist)

    dates = []
    itemdict = data[0]["timelineitems"][0]
    prevdict = __errorCaseDict()
    for date, casedictionary in itemdict.items():
        if(date=="stat"): continue

        cases = __blankCaseDict()

        if(prevdict["Confirmed"] > casedictionary["total_cases"]):
             cases["Confirmed"] = prevdict["Confirmed"]
        else:
            cases["Confirmed"] = casedictionary["total_cases"]

        if(prevdict["Deaths"] > casedictionary["total_deaths"]):
            cases["Deaths"] = prevdict["Deaths"]
        else:
            cases["Deaths"] = casedictionary["total_deaths"]

        if(prevdict["Recovered"] > casedictionary["total_recoveries"]):
            cases["Recovered"] = prevdict["Recovered"]
        else:
            cases["Recovered"] = casedictionary["total_recoveries"]

        cases["Active"] = cases["Confirmed"]-cases["Deaths"]-cases["Recovered"]

        converteddate = __convertSlashDate(date)

        prevdict = cases

        dates.append({"date":converteddate, "cases":cases})

    #Get the path to the json file for the given country
    path = __getCountryJson(country)

    newinfodict = {"country":country,"slug":slug,"file":path,"dates":dates}

    if(index < len(countrieslist)): countrieslist[index] = newinfodict
    else: countrieslist.append(newinfodict)

    #Rewrite the json file
    fileManager.writeList(countriesjsonpath,"countries",countrieslist)

def __parseProvinces(country,provinces):
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
            currDate = __convertDatetimeString(datetime.today() - timedelta(days=i))
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

#region JSON Retrieval Methods
def __getResponse(request):
    try:
        response = requests.get(request)
        print(response)
        return(response.json())
    except (ConnectionError, ConnectionRefusedError, ConnectionResetError) as e:
        print("Could not connect to API...")
    except json.decoder.JSONDecodeError:
        print("API Error...")

    return None

def findProvinceJson(countryslug, province, date):

    countryname = slugtoname[countryslug]
    provincejsonname = __jsonnameConversion(province)

    provincepath = f"JSON/Countries/{countryname}/{province}/{provincejsonname}.json"

    try:
        #Searches through the countries json file to pick the appropriate country's case numbers
        if(fileManager.exists(provincepath)):

            provincejson = fileManager.readJson(provincepath)
            cases = [dateval["cases"] for dateval in provincejson["dates"] if dateval["date"] == date]

            #Provided the country exists in the database the country's case counts will be returned
            if cases != []: return cases[0]

    except IndexError:
        pass

    #If the country's case counts can not be found the following will be executed
    #Fetch most recent data from Covid19 API and update the JSON directory
    updateProvincesJson(countryslug)
    return None

def updateProvincesJson(countryslug):
    print(f"Fetching {countryslug}'s provinces data from API...")
    data = __getResponse("https://api.covid19api.com/live/country/" + countryslug)
    if data != None: __storeAsJson(data, provinces=True)

def findCountryJson(countryslug, date):
    try:
        #Searches through the countries json file to pick the appropriate country's case numbers
        if(fileManager.exists(countriesjsonpath)):

            countries = fileManager.readJson(countriesjsonpath)
            targetcountry = [country for country in countries["countries"] if country["slug"] == countryslug]
            for i in range(len(targetcountry[0]["dates"])):
                cases = [country["dates"][i]["cases"] for country in countries["countries"] if country["slug"] == countryslug and country["dates"][i]["date"] == date]

                #Provided the country exists in the database the country's case counts will be returned
                if cases != []: return cases[0]

    except IndexError:
        pass

    updateCountryJson(countryslug)
    pass

def updateCountryJson(countryslug):
    print("Fetching country data from API...")
    data = __getResponse("https://api.thevirustracker.com/free-api?countryTimeline=" + slugtoalpha2[countryslug])
    if data != None: __storeAsJson(data, country=True, countryslug=countryslug)

def findContinentJson(continent, date):
    pass

def updateContinentsJson():
    print("Fetching continental data from API...")
    data = __getResponse("https://corona.lmao.ninja/v2/continents?yesterday=true&sort")
    if data != None: __storeAsJson(data, continents=True)


def findWorldwideJson(date):
    pass

def updateWorldwideJson():
    print("Fetching worldwide data from API...")
    data = requests.get("https://api.thevirustracker.com/free-api?global=stats")
    if data != None: __storeAsJson(data, worldwide=True)

#endregion JSON Retrieval Methods

#region Get Case Dictionary Methods
#Returns a dictionary with Covid-19 Case counts
def getCases(worldwide=False, continent=None, country="canada", province=None, attempts=3, date=datetime.today()-timedelta(days=1)):

    cases = {}

    datestring = __convertDatetimeString(date)

    #Determine whether to look for worldwide, continental, country or province info
    if(worldwide):
        cases = findWorldwideJson(datestring)

    elif(continent != None):
        cases = findContinentJson(continent, datestring)

    elif(province == None):
        cases = findCountryJson(country, datestring)

    else:
        cases = findProvinceJson(country, province, datestring)

    if cases != None: return cases

    #Could not find data after x attempts, returns an invalid case dictionary
    if(attempts == 0): return __errorCaseDict()
    #Otherwise try again now that data has been retrieved

    else: return getCases(worldwide=worldwide, continent=continent, country=country, province=province, attempts=(attempts-1), date=date)

def getCasesList(worldwide=False, continent=None, country="canada", province=None, startdate="2020-01-27", enddate=datetime.today()-timedelta(days=1)):
    caselist = []
    #Earliest date provided by the API
    mindate = __convertStringDatetime("2020-01-27")
    maxdate = datetime.today()-timedelta(days=1)

    currentdate = __convertStringDatetime(startdate)

    if currentdate < mindate:
        currentdate = mindate
    if enddate > maxdate: enddate = maxdate

    while __convertDatetimeString(currentdate) !=  __convertDatetimeString(enddate):
        caselist.append({"date":__convertDatetimeString(currentdate), "cases":getCases(worldwide=worldwide, continent=continent, country=country, province=province, attempts=0, date=currentdate)})
        currentdate += timedelta(days=1)

    return caselist
#endregion Get Case Dictionary Methods