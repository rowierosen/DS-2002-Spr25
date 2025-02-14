#!/usr/bin/python3

import os
import json
import requests
GHUSER = os.getenv('GITHUB_USER')

#print(GHUSER)

#construct url
url = 'https://api.github.com/users/{0}/events'.format(GHUSER)


#print(url)


#get data from the GitHub API
response = requests.get(url)

#successful
if response.status_code == 200:
   
    r = json.loads(response.text)

   
    print(json.dumps(r, indent=4))

  
    print("\nRecent GitHub Events:")
    for x in r[:5]:  # Limit to first 5 events
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)
else:
    print("Error fetching data:", response.status_code)

