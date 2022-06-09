from lib2to3.pgen2 import token
import paho.mqtt.client as mqtt
import time

token = "5LBFQPLtccXOPN2O0d1N"
broker = "demo.thingsboard.io"
port = 1883
toPic = "v1/devices/me/telementry"

def on_connect(client, userdata, flags, rc) :
    if (rc==0) :
        print("connected OK Returned code = ", rc)
    else :
        print("Bad connection Returned code = ", rc)
    
def on_message(client, userdata, msg) :
    print (msg.topic + " " + str(msg.payload))    

connected = False
messageRecieved = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(token)
client.connect(broker , port, 60)

client.loop_start()
client.subscribe(toPic)
while connected != True:
    time.sleep(0.2)
while messageRecieved != True:
    time.sleep(0.2)

client.loop_stop()