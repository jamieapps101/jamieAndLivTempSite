#! /usr/bin/python3


# enable debugging
import cgitb
cgitb.enable()

#print("Content-Type: text/plain;charset=utf-8")
#print()

#print("Hello World!")


import json
import pprint
import urllib


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html'),("Access-Control-Allow-Origin","*")])
    #pprint.pprint(env)
    #print("I got: \n{}\n".format(env["QUERY_STRING"]))
    data = dict(urllib.parse.parse_qsl(env["QUERY_STRING"]))
    for key in data:
        try:
            data[key] = int(data[key])
        except:
            print(data)
            exit()
    result = {"result":data["a"] + data["b"]}
    yield json.dumps(result).encode("utf-8")
    #yield str("hello").encode('utf-8')

