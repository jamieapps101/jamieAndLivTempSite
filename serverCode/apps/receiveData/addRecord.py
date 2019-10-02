#! /usr/bin/python3

import cgitb
cgitb.enable() # enable debugging


import json
import pprint
import urllib
import mysql.connector
import time
import datetime

def application(env, start_response):
    #start_response('200 OK', [('Content-Type','application/json')])
    start_response('200 OK', [('Content-Type','text/html')])

    #pprint.pprint(env)
    #print("I got: \n{}\n".format(env["QUERY_STRING"]))
    data = dict(urllib.parse.parse_qsl(env["QUERY_STRING"]))

    for key in data:
        try:
            data[key] = float(data[key])
        except:
            print(data)
            return json.dumps({"Result":"Fail"}).encode("utf-8")

    success = True
    unixTime = time.time()
    now = datetime.datetime.now()
    dateString = now.strftime("%H:%M:%S %d/%m/%Y")
    SQLdata = [0.0,0.0,0.0]
    fields = ["temperature","humidity","pressure"]
    if len(data) == 3 and all([field in data for field in fields]):
        for index in range(3):
            key = fields[index]
            SQLdata[index] = data[key]
        # do sql operations here
        mydb = mysql.connector.connect(
           host="localhost",
           user="applicationUser",
           passwd="applicationPassword",
           database = "sensorData"
        )
        dbcursor = mydb.cursor()
        command = "INSERT INTO log VALUES (" # need to craft a command
        command += unixTime + ", "
        command += dateString + ", "
        command += SQLdata[0] + ", "
        command += SQLdata[1] + ", "
        command += SQLdata[2] + ");"
        dbcursor.execute(command)
        yield json.dumps({"Result":"Success"}).encode("utf-8")
    else:
       yield json.dumps({"Result":"Fail"}).encode("utf-8")
    yield str("You tried to add data").encode('utf-8')
