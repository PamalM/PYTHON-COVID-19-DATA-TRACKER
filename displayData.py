#This (.py) handles the display of data.
#When user makes a selection on the main.py, they are directed to this script upon the ['Next'] button click.

#For reference, please remember that the countries are associated with an integer value, that is specific to each country.
#Where, [USA = 0, CANADA = 1, FRANCE = 2, U.K = 3, SPAIN = 4, ITALY = 5, WORLDWIDE = 6]

import APIInterpreter as interpreter

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
    displayValues = interpreter.getCases(slug)
    print(displayValues)

for i in range(5):
    display(i)




