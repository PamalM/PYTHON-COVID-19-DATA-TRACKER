#This (.py) handles the display of data.
#When user makes a selection on the main.py, they are directed to this script upon the ['Next'] button click.

import requests

#Each country is associated with it's own API request url.

def display(countrySlug):
    response = requests.get("https://api.covid19api.com/live/country/" + countrySlug)
    print(response.text.encode('utf8'))

