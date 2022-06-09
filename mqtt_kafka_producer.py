from random import uniform
import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
import csv
import pandas as pd

ACCESS_TOKEN='S67StJgKRRfTy7b6eVQW'                 #Token of your device
broker="demo.thingsboard.io"   			    #host name
port=1883 					    #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client1.connect(broker,port,keepalive=60)           #establish connection

while True:
    humRand = uniform(40.0, 70.0)
    temRand = uniform(20.0, 40.0)
    myData = {
        "Humidity" : humRand,
        "Temperature" : temRand
    }
    myJSon = json.dumps(myData)
    payload = str(myJSon)
    ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(1)