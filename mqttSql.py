import time
import paho.mqtt.client as mqtt
import sys
import os
import subprocess, signal, time
import socket
import sys

#-------------------------Sesi komunikasi dengan server-----------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# server_address = ('10.30.40.23', 3040)
server_address = ('localhost', 3040)

print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

#-------------------------Sesi berhenti sejenak------------------------
brokerHost = "10.30.40.23"
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
  if(receivedMessage > '0'):
  	dataFinger = receivedMessage
  	print("Sending: " + dataFinger)
  	sock.sendall(dataFinger.encode('utf-8'))
  elif(receivedMessage == 'Initializing'):
  	print("Initializing, try again")




clientMqtt = mqtt.Client()

def main():
  clientMqtt.on_message = on_message_on
  clientMqtt.on_connect = on_connect_on
  print("connecting to broker: ", brokerHost)
  clientMqtt.connect(brokerHost, port)

  clientMqtt.loop_forever()

if __name__ == "__main__":
    main()

