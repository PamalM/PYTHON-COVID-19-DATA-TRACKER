# This (.py) handles the display of data, and fetching of information for countries.
# We will make the API request and fetch information as needed, if it is out of date.
# When user makes a selection on the main.py, they are directed to this script upon the ['Next'] button click.

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
    print(slug+":",displayValues)

for i in range(5):
    display(i)


