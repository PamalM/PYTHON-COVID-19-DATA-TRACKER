import json
import requests
from datetime import datetime, timedelta
import fileManager

#TODO getCases doesn't check whether the latest data has been pulled

#TODO getAllCases will return a list of all case dictionaries for the specified country

#Reformats the returned json and organizes information into subdirectories
def parseJson(data, slug):
    #Get country name
    country = data[0]["Country"]

    #Get list of provinces
    provinces = []
    [provinces.append(value["Province"]) for value in data if(value["Province"] not in provinces)]

    #Find the earliest date listed
    earliestdate = datetime.today()
    for value in data:
        string = f'{value["Date"][0:10]} 00:00:00.000000'
        tempdate = datetime.strptime(string,'%Y-%m-%d %H:%M:%S.%f')
        if(tempdate < earliestdate):
            earliestdate = tempdate

    dates = []
    while str(earliestdate)[0:10] != str(datetime.today()+timedelta(days=1))[0:10]:
        dates.append(str(earliestdate)[0:10])
        earliestdate += timedelta(days=1)

    #Get list of dates for each province
    for province in provinces:
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
    cases = []
    provincecount = fileManager.directoryCount(dirpath)
    #Get the total count of case values across all provinces
    init = False
    for i in range(provincecount):
        try:
            province = fileManager.readJson(f"{dirpath}/{jsonname}.json")["provinces"][i]
            provincename = province["province"]
            provincejsonname = provincename.lower().replace(" ","-")

            datecount = fileManager.directoryCount(f"{dirpath}/{provincename}")

            for j in range(datecount):
                datesfile = fileManager.readJson(f"{dirpath}/{provincename}/{provincejsonname}.json")["dates"][j]
                date = datesfile["date"]
                try:
                    if not init:
                        newdict = {"date":date,"cases":{"confirmed": 0,"deaths": 0,"recovered": 0,"active": 0}}
                        cases.append(newdict)

                    #If the directory contains a total count of cases across all provinces
                    #use that information
                    if provincename == "All Provinces":
                        cases[j]["cases"] = province["cases"]
                        continue
                    #Sum up the cases from all the listed provinces
                    # print(province["cases"])
                    cases[j]["cases"]["confirmed"] += datesfile["cases"]["confirmed"]
                    cases[j]["cases"]["deaths"] += datesfile["cases"]["deaths"]
                    cases[j]["cases"]["recovered"] += datesfile["cases"]["recovered"]
                    cases[j]["cases"]["active"] += datesfile["cases"]["active"]


                except KeyError:
                    continue
            init = True
        except IndexError:
            continue

    #Create the json file for the given country
    path = f"JSON/Countries/{country}/{jsonname}.json"
    newinfodict = {"country":country,"slug":slug,"file":path,"dates":cases}

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

    index = 0

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
                foundfromapi = False
                #Retrive date's statistics
                confirmed = 0
                deaths = 0
                recovered = 0
                active = 0
                for value in data:
                    if(value["Date"].startswith(date) and value["Province"] == checkprovince):
                        confirmed = value["Confirmed"]
                        deaths = value["Deaths"]
                        active = value["Active"]
                        recovered = value["Recovered"]
                        foundfromapi = True
                        break
                if(not foundfromapi):
                    try:
                        prevdate = fileManager.readJson(f"JSON/Countries/{country}/{province}/{dates[index-1]}/{dates[index-1]}.json")
                        confirmed = prevdate["confirmed"]
                        deaths = prevdate["deaths"]
                        active = prevdate["active"]
                        recovered = prevdate["recovered"]
                    except FileNotFoundError:
                        p

                tempdict = {"confirmed":confirmed,"deaths":deaths,"recovered":recovered,"active":active}
                fileManager.writeJson(path,tempdict)

                newinfodict = {"date":date,"file":path,"cases":tempdict}

                dateslist.append(newinfodict)

        #Rewrite the json file
        fileManager.writeList(datesjsonpath,"dates",dateslist)
        index += 1

#Returns a dictionary with Covid-19 Case counts
def getCases(slug, attempts=3):

    #Default cases count to return if values cannot be found
    nocases = {"confirmed": -1,"deaths": -1,"recovered": -1,"active": -1}


    #Searches through the countries json file to pick the appropriate country's case numbers
    if(fileManager.exists("JSON/countries.json")):
        countries = fileManager.readJson("JSON/countries.json")
        cases = [country["dates"][len(country["dates"])-1]["cases"] for country in countries["countries"] if country["slug"] == slug and country["dates"][len(country["dates"])-1]["date"] == str(datetime.today())[0:10]]
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

