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
urlMachines = "http://rersoftware/InfocusWeb/api/GetMachineTimeTicket.aspx?&u=viewer&p=viewer&start="+dateS+"&end="+dateE + "&idlereason=1&result=j&grouped=1"
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
print(before[2:-1])

#Add Date to JSON Schema
data_content = json.loads(before[2:-1], object_pairs_hook=OrderedDict)
for rowData in data_content :
        rowData.update({'date' : date})
        alldata += str(rowData)


####################### Update Utilization % ###########################
d = data_content
date = ""
count = 0

#Running SUM list
mlist = [{"m": "XS63", "val": 0},
{"m": "XS42", "val": 0},
{"m": "ACTIVE #1", "val": 0},
{"m": "ACTIVE #2", "val": 0},
{"m": "AWEA", "val": 0},
{"m": "AWEA PLATE", "val": 0},
{"m": "BF160#1", "val": 0},
{"m": "BF160#2", "val": 0},
{"m": "BF160#3", "val": 0},
{"m": "DIAMOND #1", "val": 0},
{"m": "DIAMOND #2", "val": 0},
{"m": "DIAMOND #3", "val": 0},
{"m": "EDM Makino 85", "val": 0},
{"m": "EDM 156W", "val": 0},
{"m": "EDM Takumi", "val": 0},
{"m": "HAAS #1", "val": 0},
{"m": "HAAS #2", "val": 0},
{"m": "ML100", "val": 0},
{"m": "ROLLER 1", "val": 0},
{"m": "ROLLER 2", "val": 0},
{"m": "ROLLER 3", "val": 0},
{"m": "TARUS", "val": 0},
{"m": "THS100X #1", "val": 0},
{"m": "TOSHIBA #1", "val": 0},
{"m": "TOSHIBA #2", "val": 0},
{"m": "TOSHIBA #3", "val": 0},
{"m": "UNISIG", "val": 0}]

## Get total on time and store in dictionary
for makino in mlist:
    for x in d:
        if (x['mname'] == makino['m']):
            if x['status'] == "On":
                makino['val'] += x['duration']
                date = (x['date'])

#Load weekly hours data into md
with open('master.json') as master_data:
    md = json.load(master_data)
master_data.close()

#Loop for every machine, update weekly hours with running %
for makino in mlist:
    for arr in md[makino['m']]:
        if arr['x'] == date:
            percentage = "{:.2f}".format(((makino['val']/totalTime)* 100))
            if ((makino['val']/totalTime)* 100 < 99.50):
                arr.update({'y' : percentage})
                #arr.update({'y' : str(makino['val'])   })
                print(str(makino['m']) + " : " +  str(makino['val']) + " @ " + str(percentage) + "%")
                log += str(makino['m']) + " : " +  str(makino['val']) + " @ " + str(percentage) + "%" + '\n'
            else:
                percentage = "100"
                print(str(makino['m']) + " : " +  str(makino['val']) + " @ " + str(percentage) + "%")
                arr.update({'y' : percentage})
                log += str(makino['m']) + " : " +  str(makino['val']) + " @ " + str(percentage) + "%" + '\n'

        else:
            count += 1

        if (count == 7):
            md[makino['m']].pop(0)
            md[makino['m']].append({"y":makino['val'], "x": date})
            count = 0
    
    count = 0

# Save output
with open("master.json", 'w') as f:
	json.dump(md, f)
f.close() 

#Log
with open("log.txt", 'w') as l:
    l.write(log)
l.close()


print("Done.\n")
