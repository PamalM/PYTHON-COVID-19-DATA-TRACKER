#This (.py) handles the display of data.
#When user makes a selection on the main.py, they are directed to this script upon the ['Next'] button click.

#For reference, please remember that the countries are associated with an integer value, that is specific to each country.
#Where, [USA = 0, CANADA = 1, FRANCE = 2, U.K = 3, SPAIN = 4, ITALY = 5, WORLDWIDE = 6]

import json
import os
import requests
import fileManager

#Each country is associated with it's own API request url.

#The API documentation for Postman has different 'slug' urls for each country.
countrySlug = {0: "united-states",
               1: "canada",
               2: "france",
               3: "united-kingdom",
               4: "spain",
               5: "italy"}

def display(countryCode):
    slug = countrySlug.get(countryCode)

    #TODO Check to see if data is already written to local json
    #TODO otherwise obtain new data from API

    #Fetch most recent data from Covid19 API and update the JSON directory
    response = requests.get("https://api.covid19api.com/live/country/" + countrySlug.get(countryCode))
    __parseJson(response.json())

    #print(response.text.encode('utf8'))


#Reformats the returned json and organizes information into subdirectories
def __parseJson(data):

    #Get country name
    country = data[0]["Country"]
    __parseCountry(country)

    provinces = []
    [provinces.append(value["Province"]) for value in data if(value["Province"] not in provinces)]
    __parseProvinces(country, provinces)

    for province in provinces:
        dates = []
        [dates.append(value["Date"][0:10]) for value in data if(value["Date"] not in dates and value["Province"] == province)]
        __parseDates(country, province, dates, data)

def __parseCountry(country):
    print("Parsing Country: "+country)

    #Check if country's directory exists, if not, create it
    fileManager.mkexistsdir(f"JSON/Countries/{country}")

    countriesjsonpath = "JSON/countries.json"

    #Check if countries json file exists, if not, create it
    fileManager.jsonPreset(countriesjsonpath,"countries")

    #Load existing countries.json file
    countrieslist = fileManager.readList(countriesjsonpath,"countries")

    #Check if the countries list already contains the country file path
    iscontained = False
    for countryinfodict in countrieslist:
        if(countryinfodict["country"] is country): iscontained = True

    #If the country isn't contained append the new country's dict to the countries list
    if not iscontained:
        #Create the json file for the given country
        filename = country.lower().replace(" ","-")
        path = f"JSON/Countries/{country}/{filename}.json"
        fileManager.jsonPreset(path,"provinces")

        newinfodict = {"country":country,"file":path}
        countrieslist.append(newinfodict)

    #Rewrite the json file
    fileManager.writeList(countriesjsonpath,"countries",countrieslist)

def __parseProvinces(country,provinces):
    for province in provinces:
        if province == "": province = "All"
        print("Parsing Province: "+province)

        #Check if province's directory exists, if not, create it
        fileManager.mkexistsdir(f"JSON/Countries/{country}/{province}")

        jsonname = country.lower().replace(" ","-")
        provincesjsonpath = f"JSON/Countries/{country}/{jsonname}.json"

        #Check if provinces json file exists, if not, create it
        fileManager.jsonPreset(provincesjsonpath,"provinces")

        #Load existing provinces.json file
        provinceslist = fileManager.readList(provincesjsonpath,"provinces")

        #Check if the provinces list already contains the province file path
        iscontained = False
        for provinceinfodict in provinceslist:
            if(provinceinfodict["province"] is province): iscontained = True

        #If the province isn't contained append the new province's dict to the provinces list
        if not iscontained:
            #Create the json file for the given province
            filename = province.lower().replace(" ","-")
            path = f"JSON/Countries/{country}/{province}/{filename}.json"
            fileManager.jsonPreset(path,"dates")

            newinfodict = {"province":province,"file":path}
            provinceslist.append(newinfodict)

        #Rewrite the json file
        fileManager.writeList(provincesjsonpath,"provinces",provinceslist)

def __parseDates(country,province,dates,data):
    for date in dates:
        #Used to check the data file with the original name of province
        checkprovince = province
        if province == "": province = "All"

        print("Parsing Date: "+date+" for Province: "+province)

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
            if(dateinfodict["date"] is date): iscontained = True

        #If the date isn't contained append the new date's dict to the dates list
        if not iscontained:
            #Create the json file for the given date
            filename = date
            path = f"JSON/Countries/{country}/{province}/{date}/{filename}.json"
            if not os.path.exists(path):
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

                f = open(path,"w+")
                tempdict = {"confirmed":confirmed,"deaths":deaths,"recovered":recovered,"active":active}
                f.write(json.dumps(tempdict))
                f.close()

            newinfodict = {"date":date,"file":path}
            dateslist.append(newinfodict)

        #Rewrite the json file
        fileManager.writeList(datesjsonpath,"dates",dateslist)

display(4)