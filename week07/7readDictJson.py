# Reads a dictionary from a JSON file
# Author: Andrew Scott

import json

filename = "testDict.json"

def readDict():
    with open(filename) as f:
        return json.load(f)
        
someDict = readDict()
print(someDict)