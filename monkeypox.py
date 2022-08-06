#!/usr/bin/python3

import requests

uri = "https://www.cdc.gov/poxvirus/monkeypox/response/2022/us-map.html"
match = "<span class=\"fs12 text-primary\"> "

req = requests.get(uri).text
loc = req.find(match) + len(match)
removeFirst = req[loc:]
cases = removeFirst[:removeFirst.find("<")]
print(f"{cases} USA cases")
