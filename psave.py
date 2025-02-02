# Parse the HTML using BeautifulSoup
import json
from bs4 import BeautifulSoup
from scraper import read, write
from parser import parse_property_data

html = read("home.html")
soup = BeautifulSoup(html, 'html.parser')

script_tag = soup.find('script', id='__NEXT_DATA__')
if script_tag:
    data = json.loads(script_tag.string)
    pd = data["props"]["pageProps"]["componentProps"]["initialReduxState"]["gdp"]["building"]
    parsed = parse_property_data(pd)
    with open('data.json', 'w') as file:
        json.dump(pd, file, indent=4)   

    print("JSON data saved to 'data.json'")
else:
    print("Script tag with id '__NEXT_DATA__' not found.")