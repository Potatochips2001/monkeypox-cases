#!/usr/bin/python3

import requests, sys, argparse, math #json is no longer needed


#This uri hasn't been updated for a long time, so I'm using another one I was able to find.
#uri = "https://www.cdc.gov/poxvirus/monkeypox/modules/data-viz/mpx_US_Total_databite.json"

uri = "https://www.cdc.gov/wcms/vizdata/poxvirus/monkeypox/data/MPX-Cases-Deaths-by-Country.csv"

country = ""

parser = argparse.ArgumentParser()
parser.add_argument("--country")
args = parser.parse_args()

if args.country == None:
    country = ""
else:
    country = args.country.lower() + ','

d = requests.get(uri)
packet_data = d.text.lower()

if country == "":
    country = "united states,"
    usa_cases_t1 = packet_data[packet_data.find(country)+len(country):]
    usa_cases = usa_cases_t1[:usa_cases_t1.find(",")]
    usa_deaths_t1 = packet_data[packet_data.find(country)+len(country)+len(usa_cases)+1:]
    usa_deaths = usa_deaths_t1[:usa_deaths_t1.find(",")]
    fatal_percentage = int(usa_deaths) / int(usa_cases)
    exit(f"cases in {country} {int(usa_cases):,}, deaths {int(usa_deaths):,}\nfatality rate: {math.floor(fatal_percentage*1000)/10}%")
else:
    try:
        country_cases_t1 = packet_data[packet_data.find(country)+len(country):]
        country_cases = country_cases_t1[:country_cases_t1.find(',')]
        country_deaths_t1 = packet_data[packet_data.find(country)+len(country)+len(country_cases)+1:]
        country_deaths = country_deaths_t1[:country_deaths_t1.find(',')]
        if country_deaths == 0:
            fatal_percentage = 0
        else:
            fatal_percentage = int(country_deaths) / int(country_cases)
        exit(f"cases in {country} {int(country_cases):,}, deaths {int(country_deaths):,}\nfatality rate: {math.floor(fatal_percentage*1000)/10}%")
    except Exception:
        exit("country not found")



