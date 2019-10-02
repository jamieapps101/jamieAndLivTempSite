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
    yield str("A").encode('utf-8')

    #pprint.pprint(env)
    #print("I got: \n{}\n".format(env["QUERY_STRING"]))
    data = dict(urllib.parse.parse_qsl(env["QUERY_STRING"]))
    yield str("B").encode('utf-8')
    for key in data:
        try:
            yield str("C").encode('utf-8')
            data[key] = float(data[key])
        except:
            yield str("D").encode('utf-8')
            print(data)
            return json.dumps({"Result":"Fail"}).encode("utf-8")
    yield str("E").encode('utf-8')
    success = True
    unixTime = time.time()
    yield str("D").encode('utf-8')
    #dateString = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.now()
    dateString = now.strftime("%H:%M:%S %d/%m/%Y")
    SQLdata = [0.0,0.0,0.0]
    yield str("E").encode('utf-8')
    fields = ["temperature","humidity","pressure"]
    gotFeilds = all([field in data for field in fields])
    yield str("F").encode('utf-8')
    success = gotFeilds

    if len(data) != 3:
        success = False
    yield str("G").encode('utf-8')
    if success == True:
        for index in range(3):
            key = fields[index]
    yield str("H").encode('utf-8')
    #        SQLdata[index] = data[key]

    # do sql operations here
    #mydb = mysql.connector.connect(
    #    host="localhost",
    #    user="applicationUser",
    #    passwd="applicationPassword",
    #    database = "sensorData"
    #)
    #dbcursor = mydb.cursor()

    #command = "INSERT INTO log VALUES (" # need to craft a command
    #command += unixTime + ", "
    #command += dateString + ", "
    #command += SQLdata[0] + ", "
    #command += SQLdata[1] + ", "
    #command += SQLdata[2] + ");"
    #dbcursor.execute(command)


    #if(success == True):
    #    yield json.dumps({"Result":"Success"}).encode("utf-8")
    #else:
    #    yield json.dumps({"Result":"Fail"}).encode("utf-8")
    yield str("You tried to add data").encode('utf-8')
