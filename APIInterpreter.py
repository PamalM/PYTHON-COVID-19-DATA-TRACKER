import json
import requests
from datetime import datetime, timedelta
import fileManager

#Reformats the returned json and organizes information into subdirectories
def parseJson(data, slug):
    #Get country name
    country = data[0]["Country"]

    #Get list of provinces
    provinces = []
    [provinces.append(value["Province"]) for value in data if(value["Province"] not in provinces)]

    #Get list of dates for each province
    for province in provinces:
        dates = []
        [dates.append(value["Date"][0:10]) for value in data if(value["Date"] not in dates and value["Province"] == province)]
        __parseDates(country, province, dates, data)

    __parseProvinces(country, provinces, data)
    __parseCountry(country, data, slug)

def __parseCountry(country,data,slug):
    countriesjsonpath = "JSON/countries.json"

    #Check if countries json file exists, if not, create it
    fileManager.jsonPreset(countriesjsonpath,"countries")

    #Get index of country in json array
    countrieslist = fileManager.readList(countriesjsonpath,"countries")
    index = 0
    for p in countrieslist:
        if p["country"] == country: break
        else: index += 1

    jsonname = country.lower().replace(" ","-")

    #Get the most recent number of cases
    dirpath = f"JSON/Countries/{country}"
    cases = {"confirmed":0,"deaths":0,"recovered":0,"active":0}
    provincecount = fileManager.directoryCount(dirpath)
    #Get the total count of case values across all provinces
    for i in range(provincecount):
        try:
            province = fileManager.readJson(f"{dirpath}/{jsonname}.json")["provinces"][i]
            #If the directory contains a total count of cases across all provinces
            #use that information
            if province["province"] == "All Provinces":
                cases = province["cases"]
                break
            #Sum up the cases from all the listed provinces
            cases["confirmed"] += province["cases"]["confirmed"]
            cases["deaths"] += province["cases"]["deaths"]
            cases["recovered"] += province["cases"]["recovered"]
            cases["active"] += province["cases"]["active"]

        except IndexError:
            continue

    #Create the json file for the given country
    path = f"JSON/Countries/{country}/{jsonname}.json"
    newinfodict = {"country":country,"slug":slug,"file":path,"cases":cases}

    if(index < len(countrieslist)): countrieslist[index] = newinfodict
    else: countrieslist.append(newinfodict)

    #Rewrite the json file
    fileManager.writeList(countriesjsonpath,"countries",countrieslist)

def __parseProvinces(country,provinces,data):
    for province in provinces:
        if province == "": province = "All Provinces"

        jsonname = country.lower().replace(" ","-")
        provincesjsonpath = f"JSON/Countries/{country}/{jsonname}.json"

        #Check if provinces json file exists, if not, create it
        fileManager.jsonPreset(provincesjsonpath,"provinces")

        #Get index of province in json array
        provinceslist = fileManager.readList(provincesjsonpath,"provinces")
        index = 0
        for p in provinceslist:
            if p["province"] == province: break
            else: index += 1

        #Get the most recent number of cases
        dirpath = f"JSON/Countries/{country}/{province}"
        cases = {"confirmed":0,"deaths":0,"recovered":0,"active":0}
        datecount = fileManager.directoryCount(dirpath)
        for i in range(datecount):
            currDate = str(datetime.today() - timedelta(days=i))[0:10]
            datepath = f"{dirpath}/{currDate}/{currDate}.json"
            if fileManager.exists(datepath):
                recent = fileManager.readJson(datepath)
                cases = recent
                break

        jsonname = province.lower().replace(" ","-")
        filepath = f"JSON/Countries/{country}/{province}/{jsonname}.json"
        newinfodict = {"province":province,"file":filepath,"cases":cases}

        if(index < len(provinceslist)): provinceslist[index] = newinfodict
        else: provinceslist.append(newinfodict)

        #Rewrite the json file
        fileManager.writeList(provincesjsonpath,"provinces",provinceslist)

def __parseDates(country,province,dates,data):
    #Used to check the data file with the original name of province
    checkprovince = province
    if province == "": province = "All Provinces"

    for date in dates:
        #Check if date's directory exists, if not, create it
        fileManager.mkexistsdir(f"JSON/Countries/{country}/{province}/{date}")

        jsonname = province.lower().replace(" ","-")
        datesjsonpath = f"JSON/Countries/{country}/{province}/{jsonname}.json"

        #Check if dates json file exists, if not, create it
        fileManager.jsonPreset(datesjsonpath,"dates")

        #Load existing dates.json file
        dateslist = fileManager.readList(datesjsonpath,"dates")

        #Check if the dates list already contains the dates file path
        iscontained = False
        for dateinfodict in dateslist:
            if(dateinfodict["date"] == date): iscontained = True

        #If the date isn't contained append the new date's dict to the dates list
        if not iscontained:
            #Create the json file for the given date
            path = f"JSON/Countries/{country}/{province}/{date}/{date}.json"
            if not fileManager.exists(path):
                #Retrive date's statistics
                confirmed = 0
                deaths = 0
                recovered = 0
                active = 0
                for value in data:
                    if(value["Date"].startswith(date) and value["Province"] == checkprovince):
                        confirmed = value["Confirmed"]
                        deaths = value["Deaths"]
                        recovered = value["Recovered"]
                        active = value["Active"]

                tempdict = {"confirmed":confirmed,"deaths":deaths,"recovered":recovered,"active":active}
                fileManager.writeJson(path,tempdict)

                newinfodict = {"date":date,"file":path,"cases":tempdict}

                dateslist.append(newinfodict)

        #Rewrite the json file
        fileManager.writeList(datesjsonpath,"dates",dateslist)

#Returns a dictionary with Covid-19 Case counts
def getCases(slug, attempts=3):

    #Default cases count to return if values cannot be found
    nocases = {"confirmed": -1,"deaths": -1,"recovered": -1,"active": -1}

    #Searches through the countries json file to pick the appropriate country's case numbers
    if(fileManager.exists("JSON/countries.json")):
        countries = fileManager.readJson("JSON/countries.json")
        cases = [country["cases"] for country in countries["countries"] if country["slug"] == slug]
        #Provided the country exists in the database the country's case counts will be returned
        if cases != []: return cases[0]

    #If the country's case counts can not be found the following will be executed

    #Fetch most recent data from Covid19 API and update the JSON directory
    print("Fetching data from API...")
    response = requests.get("https://api.covid19api.com/live/country/" + slug)
    parseJson(response.json(), slug)

    #Could not find data after x attempts, returns an invalid case dictionary
    if(attempts == 0): return nocases
    #Otherwise try again now that data has been retrieved
    else: return getCases(slug, attempts-1)