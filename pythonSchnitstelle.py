#!/usr/bin/python           # This is server.py file

import socket               
import random
from naoqi import ALProxy  
 
#Pepper
ip_addr = "10.95.249.12"
#ip_addr = "192.168.178.24"

camera = 0                                  #camera index subscribe top camera
resolution = 0                              #0=160x120 1=320x240 7=80x60 8=40x30
colorSpace = 13                             #Buffer contains triplet on the format 0xRRGGBB, equivalent to three unsigned char
fps = 30                                    #FPS
videoDevice = ALProxy('ALVideoDevice', ip_addr, 9559)

GET_VERSION     = "GET_VERSION"
GET_META_DATA   = "GET_META_DATA"
GET_IMAGE_DATA  = "GET_IMAGE_DATA"
UNKNOWN_COMMAND = "UNKNOWN COMMAND"

width  = 40*4
hight = 30*4
color  =  1
imageSize = width*hight*3     #*3 if colored image

VERSION_STRING   = "IRG STD IMG SRV 1.0.0"
META_DATA_STRING = "[W=%d,H=%d,O=W,C=%d,X=RGB,B=%d,BTS=0]" % (width, hight, color, imageSize)
UNKNOWN_RESPONSE_STRING = "%s please try:\n  %s\n  %s\n  %s\n" % (UNKNOWN_COMMAND, GET_VERSION, GET_META_DATA, GET_IMAGE_DATA)

print(VERSION_STRING)
print(META_DATA_STRING)
print(UNKNOWN_RESPONSE_STRING)


s = socket.socket()         # Create a socket object
host = socket.gethostbyname('localhost')

port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
   print "Waiting for connection."
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from: ', addr)
   captureDevice = videoDevice.subscribeCamera("test", camera, resolution, colorSpace, fps)
   print "subscribed to TopCamera"
   try:
       while True:
           request = c.recv(1024)
           print("handle request: " + request)
           result = videoDevice.getImageRemote(captureDevice);
           imageList = list(result[6])
           if request == GET_VERSION:
               c.send(VERSION_STRING);
           elif request == GET_META_DATA:
               c.send(META_DATA_STRING)
           elif request == GET_IMAGE_DATA:
               for i in range(0, imageSize):
                   c.send(imageList[i]);
           else:
               c.send(UNKNOWN_RESPONSE_STRING)
   except:
       print("Closing connection")
       c.close() # Close the connection
       videoDevice.unsubscribe(captureDevice)


