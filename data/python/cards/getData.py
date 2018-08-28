import sys
import requests
import datetime
import json
import os
import time
from datetime import datetime, timedelta
from itertools import chain
from collections import OrderedDict


######################## Get Data ##############################################
# Time Variables
tnow = datetime.now() 
unow = datetime.utcnow()
date = str(tnow.strftime('%Y-%m-%d'))
dateS = str(datetime.combine(tnow.date(), datetime.min.time()) + timedelta (hours = 4))
dateE = str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
hour = float(tnow.hour)
minute = float(tnow.minute / 60)
totalTime = hour + minute

#Machine Time Ticket URL
urlMachines = "http://rersoftware/InfocusWeb/api/getlivedata.aspx?u=viewer&p=viewer&result=j"
print("URL: " + urlMachines + '\n')

#HTTP CALL 
try:
    r = requests.get(urlMachines)
except requests.exceptions.RequestException as e: 
    print( e )
    sys.exit(1)

#Cast results to string	
before = str(r.content)

## String variables & print raw data.
log = ""
alldata = ""

## Loaded API Data
data_content = json.loads(before[2:-1], object_pairs_hook=OrderedDict)

####################### Update Utilization % ###########################
d = data_content
count = 0

# Running JSON Data
mlist = [{"m": "XS63", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "XS42", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "ACTIVE #1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "ACTIVE #2", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "AWEA", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "AWEA PLATE", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "BF160#1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "BF160#2", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "BF160#3", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "DIAMOND #1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "DIAMOND #2", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "DIAMOND #3", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "EDM Makino 85", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "EDM 156W", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "EDM Takumi", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "HAAS #1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "HAAS #2", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "ML100", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "ROLLER 1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "ROLLER 2", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "ROLLER 3", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "TARUS", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "THS100X #1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "TOSHIBA #1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "TOSHIBA #2", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "TOSHIBA #3", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": "UNISIG", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX A81", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX BELMONT", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX BF130", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX BF200", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX Diamond", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX EDM 156", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX EDM Makino 65", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX Gundrill", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""},
{"m": " MX KBT1", "job": "", "operator": "", "ipm": "", "rpm":"", "file": "", "completion": "", "proc": "", "tlines": ""}]

## Get total on time and store in dictionary
for makino in mlist:
    for x in d:
        if (x['mname'] == makino['m']):
            if x['machineprogram'] == "m":
                if x['id'] == 1:
                    makino['ipm'] = x['lvalue']
                elif x['id'] == 2:
                    makino['rpm'] = x['lvalue']
                elif x['id'] == 3:
                    makino['file'] = x['lvalue']
                elif x['id'] == 9:
                    makino['operator'] = x['lvalue']
                elif x['id'] == 11:
                    makino['completion'] = x['lvalue']
            elif x['machineprogram'] == "p":
                if x['id'] == 1:
                    makino['job'] = x['lvalue']
                elif x['id'] == 4:
                    makino['tlines'] = x['lvalue']
                elif x['id'] == 19:
                    makino['proc'] = x['lvalue']
                   
# Save output
with open("data.json", 'w') as f:
	json.dump(mlist, f)
f.close() 

for x in mlist:
    print(str(x) + "\n")

print("Done.\n")
