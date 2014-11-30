import json
from pprint import pprint
json_data=open('C:\Python34\JsonAssignment.json')

data = json.load(json_data)
pprint(data)
json_data.close()


