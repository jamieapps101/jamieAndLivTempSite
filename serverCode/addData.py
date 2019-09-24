#! /usr/bin/python3


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
    #return [start_response]



import cgitb
cgitb.enable()

import cgi
import os
import simplejson as json
import platform
import subprocess

print("Content-type: text/html\n\n") # need to do this at the start

#response["output"] = subprocess.check_call(["ls", "-l"])
form = cgi.FieldStorage() 


inputA = form.getvalue('inputA')
inputB  = form.getvalue('inputB')

response={}


response["version"] = str(platform.python_version()) + "\n"
response["input"] = {"A":inputA,"B":inputB}

response["result"] = pow(int(inputA),int(inputB))
response["info"] = os.listdir("/usr/local/bin")
#print("result: " + str(inputA + inputB))
print(json.JSONEncoder().encode(response))
