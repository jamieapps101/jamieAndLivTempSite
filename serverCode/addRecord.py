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
    start_response('200 OK', [('Content-Type','application/json'))])
    #pprint.pprint(env)
    #print("I got: \n{}\n".format(env["QUERY_STRING"]))
    data = dict(urllib.parse.parse_qsl(env["QUERY_STRING"]))
    for key in data:
        try:
            data[key] = float(data[key])
        except:
            print(data)
            exit()
    success = True
    unixTime = time.time()
    dateString = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    SQLdata = [0.0,0.0,0.0]
    feilds = ["temperature","humidity","pressure"]
    gotFeilds = all([field in data for field in fields])
    success = gotFeilds
    if len(data) != 3:
        success = False

    if success == True:
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

    command = "" # need to craft a command

    dbcursor.execute(command)


    if(success == True):
        yield json.dumps({"Result":"Success"}).encode("utf-8")
    else:
        yield json.dumps({"Result":"Fail"}).encode("utf-8")
    #yield str("hello").encode('utf-8')
