# Writes a dictionary to a JSON file
# Author: Andrew Scott

import json

filename = "testDict.json"
sample = dict(name='Bob', age=40, grades=[55,49,72])

def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump(obj, f)

writeDict(sample)


