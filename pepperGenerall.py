
## @package pepperGenerall
#  Documentation for this module.
#
#  More details.

import qi
import argparse
import sys
import time
from pepperBasic import pepperBasic
from pepperConnect import pepperConnect
from naoqi import ALProxy

## Documentation for the pepperGenerall Class.
#
#  More details.
class pepperGenerall(pepperConnect):

    ## The constructor.
    #  @param self the object pointer.
    #  @param ip ip adress of the pepper robot.
    def __init__(self,ip,sessionG=None):

        self.ipAddress=ip
        self.session = qi.Session()
        if sessionG:

            self.session=sessionG
            self.pepperBasic = pepperBasic(self.ipAddress,sessionG)
        else:
            self.connectToRobot()
            self.pepperBasic = pepperBasic(self.ipAddress, self.session)
             
    ## setHead.
    #  @param self The object pointer.
    #  @param angles list[1] containing floats.
    #  @param isAbso int 2 for True 3 for False.
    #  @param accuracy float.
    #  @param velocity float.
    def setHead (self,angels, isAbso=None, accuracy=None, velocity=None):
        if accuracy:
            acc = accuracy
        else:
            acc = 0.01
        if velocity:
            speed = velocity
        else:
            speed = 4
        if isAbso:

            if isAbso ==2:
                isAbsolute = True
                
            elif isAbso==3:
                isAbsolute = False      
        else:
            isAbsolute=True

        if (type(angels[0]) == int or type (angels[0]) == float) and (type(angels[1]) == int or type (angels[1]) == float) and (type(speed) == int or type (speed) == float):
            motion = self.session.service("ALMotion")
            names  = ["HeadYaw","HeadPitch"]
            times  = [speed,speed]
            print "isAbsolute", isAbsolute
            
            if isAbsolute == True:
                motion.angleInterpolation(names, angels, times, isAbsolute)
                io=False            
                while io != True :

                    headPitch = self.pepperBasic.getHeadPitch()
                    headYaw = self.pepperBasic.getHeadYaw()
                    if headYaw[1] >= (angels[0] - acc) and headYaw[1]<= (angels[0] + acc) :
                        print "HeadYaw position reached", headYaw[1]
                        correctionAngelYaw = 0   
                    else:
                        if headYaw[1] < angels[0]:
                            yawBool = False
                            correctionAngelYaw = 0.007
                            print "correct Yaw +++ ", self.pepperBasic.getHeadYaw()[1]
                        else:
                            yawBool = False
                            correctionAngelYaw = -0.007
                            print "correct Yaw --- " ,self.pepperBasic.getHeadYaw()[1]

                    if headPitch[1] >= (angels[1] - acc) and headPitch[1]<= (angels[1] + acc) :
                        print "HeadPitch position reached",headPitch[1]
                        correctionAngelPitch = 0
                        
                    else:
                        if headPitch[1] < angels[1]:
                            pitchBool = False
                            correctionAngelPitch = 0.007
                            print "correct Pitch +++ ", self.pepperBasic.getHeadPitch()[1] 

                        else: 
                            pitchBool = False
                            correctionAngelPitch = -0.007
                            print "correct Pitch--- ", self.pepperBasic.getHeadPitch()[1]       

                    motion.angleInterpolation(names, [correctionAngelYaw,correctionAngelPitch], [3,3], False)
                    
                    if (headYaw[1] >= angels[0] - acc and headYaw[1]<= angels[0] + acc) and (headPitch[1] >= angels[1] - acc and headPitch[1]<= angels[1] + acc) :
                        io=True
            else:
                motion.angleInterpolation(names, angels, times, isAbsolute)

            return True
        else:
            print "no valid input"

    ## setLeftArm.
    #  @param self The object pointer.
    #  @param angles list[1] containing floats.
    #  @param isAbso int 0 or 1.
    #  @param accuracy float.
    #  @param velocity float.
    #  @param elbowYawN float.
    #  @param elbowRollN float.
    #  @param wristYawN float.
    def setLeftArm(self,angel,isAbso=None , accuracy=None,velocity=None, elbowYawN=None,elbowRollN=None,wristYawN=None):
        if accuracy:
            acc = accuracy
        else:
            acc = 0.01
        if velocity:
            speed = velocity
        else:
            speed = 3
        if elbowYawN:
            elbowYaw=elbowYawN
        else:
            elbowYaw= -0.35
        if elbowRollN:
            elbowRoll=elbowRollN
        else:
            elbowRoll= -0.9 
        if wristYawN:
            wristYaw=wristYawN
        else:
            wristYaw= -1.5
        if isAbso:
            if isAbso ==1:
                isAbsolute = True
            elif isAbso==0:
                isAbsolute = False
        else:
            isAbsolute=True

        if (type(angel[0]) == int or type (angel[0]) == float) and (type(angel[1]) == int or type (angel[1]) == float) and (type(elbowYaw) == int or type (elbowYaw) == float)and(type(elbowRoll) == int or type (elbowRoll) == float)and(type(wristYaw) == int or type (wristYaw) == float)and(type(speed) == int or type (speed) == float):
            motion = self.session.service("ALMotion")
            names  = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
            angles = [angel[0],angel[1], elbowYaw,elbowRoll ,wristYaw]
            times  = [speed,speed,speed,speed,speed]
            motion.angleInterpolation(names, angles, times, isAbsolute)
            runBool = False
            print "isAbsolute", isAbsolute
            if isAbsolute:
                while runBool != True :
                    lshoulderPitch = self.pepperBasic.getLeftShoulderPitch()
                    lshoulderRoll = self.pepperBasic.getLeftShoulderRoll()
                    lelbowYaw = self.pepperBasic.getLeftElbowYaw()
                    lelbowRoll=self.pepperBasic.getLeftElbowRoll()
                    lwristYaw=self.pepperBasic.getLeftWristYaw()

                    if lshoulderPitch[1] >= (angel[0] - acc) and lshoulderPitch[1]<= (angel[0] + acc) :
                        #print "left ShoulderPitch position reached:     ", lshoulderPitch[1]
                        correctionAngelShoulderPitch = 0   
                    else:
                        if lshoulderPitch[1] < angel[0]:
                            correctionAngelShoulderPitch = 0.007
                            #print "correct left shoulderPitch +++        ", self.pepperBasic.getLeftShoulderPitch()[1]
                        else:
                            correctionAngelShoulderPitch = -0.007
                            #print "correct left shoulderPitch ---        " ,self.pepperBasic.getLeftShoulderPitch()[1]

                    if lshoulderRoll[1] >= (angel[1] - acc) and lshoulderRoll[1]<= (angel[1] + acc) :
                        #print "left ShoulderRoll position reached:      ",lshoulderRoll[1]
                        correctionAngleShoulderRoll = 0  
                    else:
                        if lshoulderRoll[1] < angel[1]:
                            correctionAngleShoulderRoll = 0.007
                            #print "correct left ShoulderPitch +++       ", self.pepperBasic.getLeftShoulderRoll()[1]
                        else: 
                            correctionAngleShoulderRoll = -0.007
                            #print "correct left ShoulderPitch ---       ", self.pepperBasic.getLeftShoulderRoll()  [1]

                    if lelbowYaw[1] >= (elbowYaw - acc) and lelbowYaw[1]<= (elbowYaw + acc) :
                        #print "left elbowYaw position reached:      ",lelbowYaw[1]
                        correctionAngleElbowYaw = 0  
                    else:
                        if lelbowYaw[1] < elbowYaw:
                            correctionAngleElbowYaw = 0.007
                            #print "correct left ElbowYaw +++        ", self.pepperBasic.getLeftElbowYaw()[1]
                        else: 
                            correctionAngleElbowYaw = -0.007
                            #print "correct left ElbowYaw ---        ", self.pepperBasic.getLeftElbowYaw()[1]

                    if lelbowRoll[1] >= (elbowRoll - acc) and lelbowRoll[1]<= (elbowRoll + acc) :
                        #print "left elbowRoll position reached:     ",lelbowRoll[1]
                        correctionAngleElbowRoll = 0  
                    else:
                        if lelbowRoll[1] < elbowRoll:
                            correctionAngleElbowRoll = 0.007
                            #print "correct left ElbowRoll +++       ", self.pepperBasic.getLeftElbowRoll()[1]
                        else: 
                            correctionAngleElbowRoll = -0.007
                            #print "correct left ElbowRoll ---       ", self.pepperBasic.getLeftElbowRoll()[1]

                    if lwristYaw[1] >= (wristYaw - acc) and lwristYaw[1]<= (wristYaw + acc) :
                        #print "left wristYaw position reached:      ",lwristYaw[1]
                        correctionAngleWristYaw = 0  
                    else:
                        if lwristYaw[1] < wristYaw:
                            correctionAngleWristYaw = 0.007
                            #print "correct left wristYaw +++         ", self.pepperBasic.getLeftWristYaw()[1] 
                        else: 
                            correctionAngleWristYaw = -0.007
                            #print "correct left wristYaw ---         ", self.pepperBasic.getLeftWristYaw()[1]

                    motion.angleInterpolation(names, [correctionAngelShoulderPitch,correctionAngleShoulderRoll,correctionAngleElbowYaw,correctionAngleElbowRoll,correctionAngleWristYaw], [5,5,5,5,3], False)
                    if (lshoulderPitch[1] >= angel[0] - acc and lshoulderPitch[1]<= angel[0] + acc) and (lshoulderRoll[1] >= angel[1] -acc and lshoulderRoll[1]<= angel[1] + acc)and (lelbowYaw[1] >= elbowYaw -acc and lelbowYaw[1]<= elbowYaw + acc)and (lelbowRoll[1] >= elbowRoll -acc and lelbowRoll[1]<= elbowRoll + acc) and (lwristYaw[1] >= wristYaw -acc and lwristYaw[1]<= wristYaw + acc) :
                        runBool = True                                    
            return True
        else:
            print "no valid input"
            return False

    ## setRightArm.
    #  @param self The object pointer.
    #  @param angles list[1] containing floats.
    #  @param isAbso int 0 or 1.
    #  @param accuracy float.
    #  @param velocity float.
    #  @param elbowYawN float.
    #  @param elbowRollN float.
    #  @param wristYawN float.
    def setRightArm(self,angel ,isAbso=None, accuracy=None,velocity=None, elbowYawN=None,elbowRollN=None,wristYawN=None):
        if accuracy:
            acc = accuracy
        else:
            acc = 0.01
        if velocity:
            speed = velocity
        else:
            speed = 3
        if elbowYawN:
            elbowYaw=elbowYawN
        else:
            elbowYaw= 0.35
        if elbowRollN:
            elbowRoll=elbowRollN
        else:
            elbowRoll= 0.9
        if wristYawN:
            wristYaw=wristYawN
        else:
            wristYaw= 1.5
        if isAbso:
            if isAbso ==1:
                isAbsolute = True
            elif isAbso==0:
                isAbsolute = False
        else:
            isAbsolute=True
   
        if (type(angel[0]) == int or type (angel[0]) == float) and (type(angel[1]) == int or type (angel[1]) == float) and (type(elbowYaw) == int or type (elbowYaw) == float)and(type(elbowRoll) == int or type (elbowRoll) == float)and(type(wristYaw) == int or type (wristYaw) == float)and(type(speed) == int or type (speed) == float):
            motion = self.session.service("ALMotion")
            names  = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
            angles = [angel[0],angel[1], elbowYaw,elbowRoll ,wristYaw]
            times  = [speed,speed,speed,speed,speed]
            #isAbsolute = True
            motion.angleInterpolation(names, angles, times, isAbsolute)
            runBool = False
            print "isAbsolute", isAbsolute

            if isAbsolute:
                while runBool != True :
                    lshoulderPitch = self.pepperBasic.getRightShoulderPitch()
                    lshoulderRoll = self.pepperBasic.getRightShoulderRoll()
                    lelbowYaw = self.pepperBasic.getRightElbowYaw()
                    lelbowRoll=self.pepperBasic.getRightElbowRoll()
                    lwristYaw=self.pepperBasic.getRightWristYaw()

                    if lshoulderPitch[1] >= (angel[0] -acc) and lshoulderPitch[1]<= (angel[0] + acc) :
                        #print "Right ShoulderPitch position reached:        ", lshoulderPitch[1]
                        correctionAngelShoulderPitch = 0   
                    else:
                        if lshoulderPitch[1] < angel[0]:
                            correctionAngelShoulderPitch = 0.007
                            #print "correct shoulderPitch +++        ", self.pepperBasic.getRightShoulderPitch()[1]
                        else:
                            correctionAngelShoulderPitch = -0.007
                            #print "correct shoulderPitch ---        " ,self.pepperBasic.getRightShoulderPitch()[1]

                    if lshoulderRoll[1] >= (angel[1] -acc) and lshoulderRoll[1]<= (angel[1] + acc) :
                        #print "Right ShoulderRoll position reached:     ",lshoulderRoll[1]
                        correctionAngleShoulderRoll = 0  
                    else:
                        if lshoulderRoll[1] < angel[1]:
                            correctionAngleShoulderRoll = 0.007
                            #print "correct right Shoulder Roll +++       ", self.pepperBasic.getRightShoulderRoll()[1]
                        else: 
                            correctionAngleShoulderRoll = -0.007
                            #print "correct right Shoulder Roll ---       ", self.pepperBasic.getRightShoulderRoll()  [1]

                    if lelbowYaw[1] >= (elbowYaw -acc) and lelbowYaw[1]<= (elbowYaw + acc) :
                        #print "Right elbowYaw position reached:     ",lelbowYaw[1]
                        correctionAngleElbowYaw = 0  
                    else:
                        if lelbowYaw[1] < elbowYaw:
                            correctionAngleElbowYaw = 0.007
                            #print "correct right ElbowYaw +++         ", self.pepperBasic.getRightElbowYaw()[1]
                        else: 
                            correctionAngleElbowYaw = -0.007
                            #print "correct right ElbowYaw ---         ", self.pepperBasic.getRightElbowYaw()[1]

                    if lelbowRoll[1] >= (elbowRoll -acc) and lelbowRoll[1]<= (elbowRoll + acc) :
                        #print "Right elbowRoll position reached:        ",lelbowRoll[1]
                        correctionAngleElbowRoll = 0  
                    else:
                        if lelbowRoll[1] < elbowRoll:
                            correctionAngleElbowRoll = 0.007
                            #print "correct right ElbowRoll +++        ", self.pepperBasic.getRightElbowRoll()[1]
                        else: 
                            correctionAngleElbowRoll = -0.007
                            #print "correct right ElbowRoll ---        ", self.pepperBasic.getRightElbowRoll()[1]

                    if lwristYaw[1] >= (wristYaw -acc) and lwristYaw[1]<= (wristYaw + acc) :
                        #print "Right wristYaw position reached:     ",lwristYaw[1]
                        correctionAngleWristYaw = 0  
                    else:
                        if lwristYaw[1] < wristYaw:
                            correctionAngleWristYaw = 0.007
                            #print "correct right wristYaw +++         ", self.pepperBasic.getRightWristYaw()[1] 
                        else: 
                            correctionAngleWristYaw = -0.007
                            #print "correct right wristYaw ---         ", self.pepperBasic.getRightWristYaw()[1]

                    motion.angleInterpolation(names, [correctionAngelShoulderPitch,correctionAngleShoulderRoll,correctionAngleElbowYaw,correctionAngleElbowRoll,correctionAngleWristYaw], [5,5,5,5,5], False)
                    if (lshoulderPitch[1] >= angel[0] -acc and lshoulderPitch[1]<= angel[0] + acc) and (lshoulderRoll[1] >= angel[1] -acc and lshoulderRoll[1]<= angel[1] + acc)and (lelbowYaw[1] >= elbowYaw -acc and lelbowYaw[1]<= elbowYaw + acc)and (lelbowRoll[1] >= elbowRoll -acc and lelbowRoll[1]<= elbowRoll + acc) and (lwristYaw[1] >= wristYaw -acc and lwristYaw[1]<= wristYaw + acc) :
                        runBool = True                                  
            return True
        else:
            print "no valid input"
            return False

if __name__ == "__main__": 
    fkt = pepperGenerall("10.95.249.12") 


