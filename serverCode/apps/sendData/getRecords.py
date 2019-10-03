#! /usr/bin/python3


import cgitb
cgitb.enable()


import json
import pprint
import urllib
import mysql.connector


def application(env, start_response):
    #start_response('200 OK', [('Content-Type','application/json')])
    start_response('200 OK', [('Content-Type','text/html')])
    try:
        # yield str("A").encode('utf-8')
        data = dict(urllib.parse.parse_qsl(env["QUERY_STRING"]))
        # yield str("B").encode('utf-8')
        if ("records" in data) and (len(data)==1):
            # yield str("C").encode('utf-8')
            recordsRequest = int(data["records"])
            mydb = mysql.connector.connect(
                host="localhost",
                user="applicationUser",
                passwd="applicationPassword",
                database = "sensorData"
            )
            # yield str("D").encode('utf-8')
            dbcursor = mydb.cursor()
            command = "SELECT * FROM log ORDER BY id DESC LIMIT " + str(recordsRequest)
            dbcursor.execute(command)
            # yield str("E").encode('utf-8')
            requestedData = dbcursor.fetchall()
            jsonData = json.dumps(requestedData)
            returnData = {"result":"success","data":jsonData}
            # yield str("F").encode('utf-8')
            yield json.dumps(returnData).encode("utf-8")
        else:
            returnData = {"result":"fail","meta":"from getRecords.py"}
            yield json.dumps(returnData).encode("utf-8")

    except Exception as e:
        return json.dumps({"Result":"fail","meta":str(e)}).encode("utf-8")
