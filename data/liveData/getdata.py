import requests
import json
import os
from itertools import chain
from collections import OrderedDict


url="http://rersoftware/InfocusWeb/api/getlivedata.aspx?u=viewer&p=viewer&result=j"

try: 
    r=requests.get(url)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)


data=str(r.content)

rawdata= json.loads(data[2:-1], object_pairs_hook=OrderedDict)

print(data)

clean = [
    {"machine" : "ACTIVE #1", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "", "status" : ""},
    {"machine" : "ACTIVE #2", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "", "status" : ""},
    {"machine" : "ROLLER 1", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "ROLLER 2", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "ROLLER 3", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "XS63", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "XS42", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "DIAMOND #1", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "DIAMOND #2", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "DIAMOND #3", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "THS100X #1", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "HAAS #1", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "HAAS #2", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "AWEA PLATE", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "AWEA", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "TOSHIBA #1", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "TOSHIBA #2", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "TOSHIBA #3", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "ML100", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "BF160#1", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "BF160#2", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "BF160#3", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "TARUS", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "UNISIG", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "EDM 156W", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "EDM Takumi", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""},
    {"machine" : "EDM Makino 85", "job" : "", "operator": "", "ipm": "","rpm" : "","file" : "","ptop" : "","pbot" : "","procedure" : "" , "status" : ""}
    ]

for line in rawdata:
    for m in clean:
        if (line['mname'] == m['machine']):
            if (line['machineprogram'] == 'm'):
                if (line['id'] == 1):
                    m['ipm'] = line['lvalue']
                elif (line['id'] == 2):
                    m['rpm'] = line['lvalue']
                elif (line['id'] == 3):
                    m['file'] = line['lvalue']
                elif (line['id'] == 11):
                    m['ptop'] = line['lvalue']
                elif (line['id'] == 9):
                    m['operator'] = line['lvalue']
                elif (line['id'] == 8):
                    m['status'] = line['lvalue']
            elif (line['machineprogram'] == "p"):
                if (line['id'] == 1):
                    m['job'] = line['lvalue']
                elif (line['id'] == 3):
                    m['procedure'] = line['lvalue']
                elif (line['id'] == 4):
                    m['pbot'] = line['lvalue']
            
        


for x in clean:
    print(x)

with open("cardData.json", 'w') as f: 
    json.dump(clean, f)
f.close()
