#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-


## @package reaching.
#  Documentation for this module.
#
#  More details.
#  


import socket               
import time
import argparse
import time
import qi
import random
from pepperArmHead import pepperArmHead
from pepperGenerall import pepperGenerall
from pepperBasic import pepperBasic
from naoqi import ALProxy
from threading import Thread

#-Global Variables
width = 0
hight = 0
speed=2
pitch = 0
yaw = 0
shoulderRollNew=0
shoulderPitchNew =0
#-

#IP address of the PepperRobot
ip = "10.95.249.12"
#ip = "192.168.178.24"

pepM = pepperGenerall(ip)
pep = pepperArmHead(
    "name",2,[
    [[-0.701, 0.101],[-0.727, 0.416],[-0.252 ,0.703],[-0.399 ,0.101]],
    [[-0.399,0.078],[-0.385,0.446],[-0.054,0.652],[-0.054,0.003]],
    [[-0.680, -0.163],[-0.739, -0.482],[-0.255 ,-0.793],[-0.324 ,-0.147]],
    [[-0.324,-0.147],[-0.325,-0.532],[0.270,-0.790],[0.101,-0.049]]
    ],
    0, #Arm
    [[0.313, -0.117],[0.181, 0.230],[-0.342, -0.126],[-0.242,0.287]], #Workspaces
    ip
	)


## This thread connects to the Blob-detector and recives the position of the Blob.
#  this thread only writes the Global Variables(width, hight).
def thread1(threadname):
    global width
    global hight
    global speed
    try:
        s = socket.socket()         # Create a socket object
        host = '10.95.249.40'       #socket.gethostname() # Get local machine name
        #host= "192.168.178.44"
        port = 34567                # Reserve a port for your service.
        s.connect((host, port))
    except:
        print "couldn't connect to Blob-Detector"
    while True:
        try:
            s.send("GET_IMAGE_DATA")
            response = s.recv(1024)
            liste = list(response)
            width = ord(liste[0]) 
            hight = ord(liste[2])
            if width in range(65,85) and hight in range(45,75):

                speed = 2

            else:

                speed = 1

        except:
            print"lost connection to Blob-detector"
            time.sleep(1)
	

## This thread reads the Global Variables (width, hight) and sets the Head in motion so it centers the blob.
#  reading globale variables.
def thread2(threadname):

    offset = 5              #offsetPixel
    midPicturehight = 60    #middelPixel of the Picture hight
    midPicturewidth = 80    #middlePixel of the Pictre width
    while True:
        
        try:
                if hight == 0:
                    inputPitch = False
                    pitch = 0
                    

                elif hight >midPicturehight + offset:
                    print "kopf runter"
                    pitch = 0.01
                    pitchBool = False
                    inputPitch = True

                elif hight <midPicturehight - offset:
                    print "kopf hoch"
                    pitch = -0.01
                    pitchBool = False
                    inputPitch = True

                else:
                    pitch = 0
                    pitchBool = True
                    inputPitch=True
                

                if width == 0: 
                    yawBool=False
                    inputYaw=False
                    yaw = 0
                elif width >midPicturewidth + offset:
                    yawBool=False
                    inputYaw=True
                    yaw = -0.01

                elif width <midPicturewidth - offset:
                    yawBool=False
                    inputYaw=True
                    yaw = 0.01
                else:
                    yawBool=True
                    yaw = 0
                    inputYaw=True
                if inputPitch == False and inputYaw==False:
                    time.sleep(0.2)
                    
                else:
                    if pitchBool == True and yawBool == True:
                        print "Object centered"
                        time.sleep(0.1) 
                    else:
                        angles = [yaw,pitch]
                        if speed ==1:
                            yaw=yaw*12
                            pitch = pitch*12
                            angles = [yaw,pitch]

                        pepM.setHead(angles,3,1,speed)
        except:
            print"Error Thread 2"


## This thread connects to the xml-Server, sends the current headposition and revives the nearest headposition and the shoulder pitch and roll.
#  writing the global variables.
def thread3(threadname):
    global shoulderPitchNew
    global shoulderRollNew 
     

    while True:
        try:
            s2 = socket.socket()             #Create a socket object                               
            host2 =  '10.95.249.40'          #socket.gethostbyname('localhost')
            #host2= "192.168.178.44"
            port2 = 56789                    #Reserve a port for your service.
            s2.connect((host2,port2))
            headPosition = pep.getCurrentHeadPosition()
            headPositionToSend= str(headPosition[0])+" "+str(headPosition[1])
            s2.send(headPositionToSend)     #send current headposition
            recivedData = s2.recv(1024)     #recive new data
            recivedDataProcessed= recivedData.split("\t")
            recivedDataProcessedAndSplit = recivedDataProcessed[3].split("\x00")
            shoulderPitchNew = float(recivedDataProcessed[2])
            shoulderRollNew = float(recivedDataProcessedAndSplit[0])
        except:
            print"Error xml-Server"

## This thread reads the Globalvariables shoulder pitch and roll and sets the left arm.
#  reading globale variables.
def thread4(threadname):
    pepMleft = pepperGenerall(ip)
    while True:
        try:
            speed=2
            if hight ==0 and width==0:
                    pass
                    #no input
            else:
                if shoulderRollNew >0:
                    print "use left Arm"
                    angel=[shoulderPitchNew,shoulderRollNew]
                    pepMleft.setLeftArm(angel,1,1,speed,-0.35,-0.9 ,-1.5)
                else:
                    print "left arm default"
                    angel =[1.5,-0.14]
                    pepMleft.setLeftArm(angel,1,1,speed,-1.225,-0.52,-1.5)
        except:
            print"Error Thread 4"

## This thread reads the Globalvariables shoulder pitch and roll and sets the right arm.
#  reading globale variables.
def thread5(threadname):
    pepMright = pepperGenerall(ip)
    while True:
        try:
            speed=2
            
            if hight ==0 and width==0:
                pass
                #no input
            else:
                
                if shoulderRollNew < 0:
                    print "use right arm"
                    angle=[shoulderPitchNew,shoulderRollNew]
                    pepMright.setRightArm(angle,1,1,speed,0.35,0.9 ,1.5)
                else:
                    print "right arm default"
                    angle = [1.5,-0.14]
                    pepMright.setRightArm(angle,1,1,speed,1.225,0.52,1.5)
        except:
            print"Error Thread 5"



thread1 = Thread(target=thread1, args=("Thread-1",))
thread2 = Thread(target=thread2, args=("Thread-2",))
thread3 = Thread(target=thread3, args=("Thread-3",))
thread4 = Thread(target=thread4, args=("Thread-4",))
thread5 = Thread(target=thread5, args=("Thread-5",))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()




