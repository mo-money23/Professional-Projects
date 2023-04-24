from csv import excel, writer
from gettext import install
from itertools import count
import os
import subprocess
import json
import pandas as pd
import openpyxl

# Set file paths
jsonFolderPath = '[Enter Location of JSON data]' # Folder where JSONs are located
excelFilePath = '[Enter Location of excel file]' # Folder or location of the Excel for output

# Set the parameters for the excel spreadsheet
wb = openpyxl.load_workbook(excelFilePath)
writer = pd.ExcelWriter(excelFilePath, engine='openpyxl')
writer.book = wb
writer.sheets = {ws.title: ws for ws in wb.worksheets}

# Locate the files that end with .json
jsonFiles = [jsonPos for jsonPos in os.listdir(jsonFolderPath) if jsonPos.endswith('.json')]

# Create a list for the name of each JSON file (usually the name of the table)
nameLst = []
for i in jsonFiles:
    nameDict = {}
    tempTuple = os.path.splitext(i)
    jsonName = tempTuple[0]
    nameLst.append(jsonName)

df1 = pd.DataFrame(nameLst) # Create a dataframe of that list

# Create a list of the data within each JSON
fileLst = []
for i in jsonFiles:
    jsonFilePath = os.path.join(jsonFolderPath,i)
    with open (jsonFilePath, "r") as jsonFile:
        jsonData = json.load(jsonFile)
    df = pd.json_normalize(jsonData) 
    fileLst.append(df)

# Create a formatted dataframe that gets appended to the excel spreadsheet
for i in fileLst:
    df2 = pd.DataFrame(data = i)
    for sheetname in writer.sheets:
        df2.to_excel(writer, sheet_name=sheetname, startrow=writer.sheets[sheetname].max_row, index=False, header=False)

# Replace the first column with the table name (JSON File name)
for sheetname in writer.sheets:
    df1.to_excel(writer, sheet_name=sheetname, startrow=1, index=False, header=False)

writer.save()

    

    
