import requests
import json
import time

timestr = time.strftime("%Y%m%d")


url_counties = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_county_condensed_data"
url_country = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data"
url_historical = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_trends_data"

response = requests.get(url_counties)
data = response.json()

with open("data/cdc_data.json", "w") as outfile:
    json.dump(data, outfile)
    
with open(f"data/{timestr}_cdc_data.json", "w") as outfile2:
    json.dump(data, outfile2)

country_response = requests.get(url_country)
country_data = country_response.json()

with open(f"data/{timestr}_country_data.json", "w") as country_outfile:
    json.dump(country_data, country_outfile)

response_historical = requests.get(url_historical)
historical_data = response_historical.json()

with open(f"data/{timestr}_us_historical.json", "w") as historical_outfile:
    json.dump(historical_data, historical_outfile)

    
with open(f"data/_us_historical.json", "w") as historical_outfile2:
    json.dump(historical_data, historical_outfile2)
