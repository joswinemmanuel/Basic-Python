# wget https://practical.learnpython.dev/code/cities.json 
# this command will download cities.json into the location

import json
from pprint import pprint

with open("cities.json") as f:
    content = json.load(f)
    print(content)
    pprint(content)

# json.load(f) gives a list of dictinory