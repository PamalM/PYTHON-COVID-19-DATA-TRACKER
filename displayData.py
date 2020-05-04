#This (.py) handles the display of data.
#When user makes a selection on the main.py, they are directed to this script upon the ['Next'] button click.

#For reference, please remember that the countries are associated with an integer value, that is specific to each country.
#Where, [USA = 0, CANADA = 1, FRANCE = 2, U.K = 3, SPAIN = 4, ITALY = 5, WORLDWIDE = 6]

import main
import requests

def display(countryCode):
    response = requests.get("https://api.covid19api.com/live/country/canada")
    print(response.text.encode('utf8'))


#For testing purposes just run data for U.S.A currently.
display(0)
