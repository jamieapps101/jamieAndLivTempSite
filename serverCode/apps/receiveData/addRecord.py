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
    try:
        data = dict(urllib.parse.parse_qsl(env["QUERY_STRING"]))

        for key in data:
            try:
                data[key] = float(data[key])
            except:
                print(data)
                return json.dumps({"Result":"Fail"}).encode("utf-8")

        fields = ["temperature","humidity","pressure"]
        if len(data) == 3 and all([field in data for field in fields]):
            unixTime = time.time()
            now = datetime.datetime.now()
            dateString = now.strftime("%H:%M:%S %d/%m/%Y")
            SQLdata = [0.0,0.0,0.0]
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
            command = "INSERT INTO log (unixTime,time,temperature,humidity,preasure) VALUES (" # need to craft a command
            command += str(unixTime) + ", "
            command += "\"" + dateString + "\", "
            command += str(SQLdata[0]) + ", "
            command += str(SQLdata[1]) + ", "
            command += str(SQLdata[2]) + ");"
            #yield ("Command: " + command).encode('utf-8')
            dbcursor.execute(command)
            mydb.commit()
            yield json.dumps({"Result":"success"}).encode("utf-8")
        else:
           yield json.dumps({"Result":"fail","meta": "from addRecord.py"}).encode("utf-8")
    except Exception as e:
    	#yield str("You tried to add data").encode('utf-8')
        yield str(e).encode('utf-8')
	#yield json.dumps({"Result":"fail","meta": "from addRecord, script failure"}).encode("utf-8")
