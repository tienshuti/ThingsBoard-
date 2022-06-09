from random import uniform
import random
import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
import csv
import pandas as pd

ACCESS_TOKEN='DkH6pU2znndo8pKerb5T'                 #Token of your device
broker="demo.thingsboard.io"   			    #host name
port=1883 					    #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client3= paho.Client("control1")                    #create client object
client3.on_publish = on_publish                     #assign function to callback
client3.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client3.connect(broker,port,keepalive=60)           #establish connection

df = pd.read_csv("DailyDelhiClimateTrain.csv")

temperature = df['meantemp'].tolist()
humidity = df['humidity'].tolist()
windSpeed = df['wind_speed'].tolist()
i = 0

while True:
    i += 1
    wind = windSpeed[i]
    myData = {
        "Temperature" : wind
    }
    myJSon = json.dumps(myData)
    payload = str(myJSon)
    ret= client3.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(1)