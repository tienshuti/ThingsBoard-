from random import uniform
import random
import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
import csv
import pandas as pd

ACCESS_TOKEN='ICqy0r8o8KmiCjsOEyA5'                 #Token of your device
broker="demo.thingsboard.io"   			    #host name
port=1883 					    #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client2= paho.Client("control1")                    #create client object
client2.on_publish = on_publish                     #assign function to callback
client2.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client2.connect(broker,port,keepalive=60)           #establish connection

df = pd.read_csv("DailyDelhiClimateTrain.csv")

temperature = df['meantemp'].tolist()
humidity = df['humidity'].tolist()
windSpeed = df['wind_speed'].tolist()
i = 0

while True:
    i += 1
    hum = humidity[i]
    myData = {
        "Temperature" : hum
    }
    myJSon = json.dumps(myData)
    payload = str(myJSon)
    ret= client2.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(1)