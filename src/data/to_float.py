import json

with open('D:/UNI/TFG/Dashboard/updated-file.json', 'rb') as fp:
    data = json.load(fp)

for obj in data:
    obj["value"] = float(obj["value"])

with open('D:/UNI/TFG/Dashboard/updated-file.json', "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)