import json

with open('D:/UNI/TFG/Dashboard/src/data/node2_1.json', 'rb') as fp:
    jsondata = json.load(fp)


jsondata = [obj for obj in jsondata if float(obj['value']) > 2]

open("updated-file.json", "w").write(
    json.dumps(jsondata, indent=4)
)
