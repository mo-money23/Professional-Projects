import os
import json
import pandas as pd
from pickle import TRUE

# Assign location of folder containing JSON files
jsonFolderPath = '[Enter Folder Location]'

# Locates files that end with .json
jsonFiles = [jsonPos for jsonPos in os.listdir(jsonFolderPath) if jsonPos.endswith('.json')]

# Loops through  each JSON and standardizes its format
for i in jsonFiles:
    jsonFilePath = os.path.join(jsonFolderPath,i)
    with open (jsonFilePath, "r") as f:
        jsonData = json.load(f)
        cleanJson = json.dumps(jsonData, indent=4, sort_keys=TRUE)
    with open (jsonFilePath, "w") as f:
        f.write(cleanJson)





        