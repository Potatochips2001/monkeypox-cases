#!/usr/bin/python3

import requests, json, sys

#REMOVED OLD
#uri = "https://www.cdc.gov/poxvirus/monkeypox/response/2022/us-map.html"
#match = "<span class=\"fs12 text-primary\"> "

#req = requests.get(uri).text
#loc = req.find(match) + len(match)
#removeFirst = req[loc:]
#cases = removeFirst[:removeFirst.find("<")]
#print(f"{cases} USA cases")

uri = "https://www.cdc.gov/poxvirus/monkeypox/modules/data-viz/mpx_US_Total_databite.json"

d = requests.get(uri); d = json.loads(d.text)
totalCases = d['data'][46]['Cases']

enum = 0
states = {}
for key in d['data']:
    states[enum] = key['Location']
    enum += 1

for state in states:
    print(f"{d['data'][state]['Location']}: {d['data'][state]['Cases']}")

print(f"\nTotal monkeypox cases: {totalCases:,}")

