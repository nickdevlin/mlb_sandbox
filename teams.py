import json
import os
import requests

URL = ('https://api.sportradar.us/mlb-t6/seasontd/2018/'
       'REG/standings.json?api_key=' + os.environ['MLB_KEY'])

r = requests.get(url=URL)

full_text = json.loads(r.text)

leagues = full_text['league']['season']['leagues']

for league in leagues:
    for division in league['divisions']:
        print(league['alias'] + " " + division['name'])
        for team in division['teams']:
            spaces = 15 - len(team['name'])
            print(team['name'] + spaces*" " +
                  str(team['win']) + '-' + str(team['loss']))
        print("**********")
