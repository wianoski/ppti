from ftplib import FTP
import time
import paho.mqtt.client as mqtt
import sys
import os
import subprocess, signal, time
import socket
import sys

host = "10.30.40.23"
uname = "biofarma_server"
upass = "biofarmasofun"
#-------------------------Sesi komunikasi dengan server-----------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (host, 3040)
# server_address = ('localhost', 3040)
print("----------------------Sesi MQTT------------------------")
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

#-------------------------Sesi berhenti sejenak------------------------



#----------------------------Sesi FTP Dimulai--------------------------
print("----------------------Sesi FTP------------------------")
ftp = FTP()
conn_server = ftp.connect(host=host, port=21, timeout=None)
print("Connected to",conn_server)
login = ftp.login(user=uname, passwd=upass)
print("Status: ",login)
#----------------------------Sesi berhenti Sejenak---------------------

port = 1883

topic1 = "pir/pirOn"
topic2 = "pir/pirOff"
topic3 = "finger/found"
topic4 = "status/device"

subTopic1 = topic1
subTopic2 = topic2
subTopic3 = topic3
subTopic4 = topic4

def on_connect_on(client, userData, flags, rc):
  # print("connect with: "+str(rc))
  print("subs with topic: ", subTopic1)
  clientMqtt.subscribe(subTopic1)

  print("subs with topic: ", subTopic2)
  clientMqtt.subscribe(subTopic2)

  print("subs with topic: ", subTopic3)
  clientMqtt.subscribe(subTopic3)

  print("subs with topic: ", subTopic4)
  clientMqtt.subscribe(subTopic4)


def on_message_on(client, userData, message):
  # print("Message: ", message.topic , " - qos=", message.qos , " - flag=", message.retain)
  receivedMessage = str(message.payload.decode("utf-8"))
  if(receivedMessage == 'Initializing'):
  	print("Initializing, try again")
  elif(receivedMessage > '0'):
  	dataFinger = receivedMessage
  	print("Sending: " + dataFinger)
  	sock.sendall(dataFinger.encode(encoding="utf-8", errors="strict"))



clientMqtt = mqtt.Client()

def main():
  clientMqtt.on_message = on_message_on
  clientMqtt.on_connect = on_connect_on
  print("connecting to broker: ", host)
  clientMqtt.connect(host, port)

  clientMqtt.loop_forever()

if __name__ == "__main__":
    main()

