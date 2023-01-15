import json
import xmltodict
from datetime import datetime
import glob

# function to add to JSON
def write_json(new_data, filename='D:/UNI/TFG/Dashboard/src/data/node2_2.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

for i in glob.glob("D:/UNI/TFG/Nodes/LocationNODE2/Full_analisys/*"):
  with open(i) as xml_file:
      data_dict = xmltodict.parse(xml_file.read())
      print(i)

  json_data = json.dumps(data_dict)

  with open("data.json", "w") as json_file:
          json_file.write(json_data)

  json_data=open('data.json')
  data=json.load(json_data)

  for obj in data['segment']['indicators']['indicator']:
      obj['date'] = str(datetime.fromtimestamp(int(data['segment']['idseg'])))
      write_json(obj) 
