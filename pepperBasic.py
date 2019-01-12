## @package pepperBasic
#  Documentation for this module.
#
#  More details.

import qi
import argparse
import sys
import time
from naoqi import ALProxy
from pepperConnect import pepperConnect
ip = "10.95.249.12"


## Documentation for pepperBasic.
#
#  More details.
class pepperBasic(pepperConnect):
    ## the constructor.
    #  @param ip ip address off the pepper robot
    def __init__(self,ip,sessionG=None):

        self.ipAddress=ip
        if sessionG:
            self.session=sessionG
        else:
            self.session = qi.Session()
            self.connectToRobot()

    

    """Laser distance sensors get functions"""
    def getLaserFront(self):
        
        device = self.session.service("ALMemory")
        laserFrontSeg01 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg01/X/Sensor/Value")
        laserFrontSeg02 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg02/X/Sensor/Value")
        laserFrontSeg03 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg03/X/Sensor/Value")
        laserFrontSeg04 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg04/X/Sensor/Value")
        laserFrontSeg05 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg05/X/Sensor/Value")
        laserFrontSeg06 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg06/X/Sensor/Value")
        laserFrontSeg07 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg07/X/Sensor/Value")
        laserFrontSeg08 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg08/X/Sensor/Value")
        laserFrontSeg09 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg09/X/Sensor/Value")
        laserFrontSeg10 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg10/X/Sensor/Value")
        laserFrontSeg11 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg11/X/Sensor/Value")
        laserFrontSeg12 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg12/X/Sensor/Value")
        laserFrontSeg13 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg13/X/Sensor/Value")
        laserFrontSeg14 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg14/X/Sensor/Value")
        laserFrontSeg15 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg15/X/Sensor/Value")
        return [laserFrontSeg01, laserFrontSeg02, laserFrontSeg03, laserFrontSeg04, laserFrontSeg05, laserFrontSeg06, laserFrontSeg07, laserFrontSeg08, laserFrontSeg09, laserFrontSeg10, laserFrontSeg11, laserFrontSeg12, laserFrontSeg13, laserFrontSeg14, laserFrontSeg15]
    def getLaserLeft(self):
        
        device = self.session.service("ALMemory")
        laserLeftSeg01 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg01/X/Sensor/Value")
        laserLeftSeg02 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg02/X/Sensor/Value")
        laserLeftSeg03 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg03/X/Sensor/Value")
        laserLeftSeg04 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg04/X/Sensor/Value")
        laserLeftSeg05 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg05/X/Sensor/Value")
        laserLeftSeg06 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg06/X/Sensor/Value")
        laserLeftSeg07 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg07/X/Sensor/Value")
        laserLeftSeg08 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg08/X/Sensor/Value")
        laserLeftSeg09 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg09/X/Sensor/Value")
        laserLeftSeg10 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg10/X/Sensor/Value")
        laserLeftSeg11 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg11/X/Sensor/Value")
        laserLeftSeg12 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg12/X/Sensor/Value")
        laserLeftSeg13 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg13/X/Sensor/Value")
        laserLeftSeg14 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg14/X/Sensor/Value")
        laserLeftSeg15 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg15/X/Sensor/Value")
        return [laserLeftSeg01, laserLeftSeg02, laserLeftSeg03, laserLeftSeg04, laserLeftSeg05, laserLeftSeg06, laserLeftSeg07, laserLeftSeg08, laserLeftSeg09, laserLeftSeg10, laserLeftSeg11, laserLeftSeg12, laserLeftSeg13, laserLeftSeg14, laserLeftSeg15]
    def getLaserRight(self):
        
        device = self.session.service("ALMemory")
        laserRightSeg01 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg01/X/Sensor/Value")
        laserRightSeg02 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg02/X/Sensor/Value")
        laserRightSeg03 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg03/X/Sensor/Value")
        laserRightSeg04 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg04/X/Sensor/Value")
        laserRightSeg05 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg05/X/Sensor/Value")
        laserRightSeg06 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg06/X/Sensor/Value")
        laserRightSeg07 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg07/X/Sensor/Value")
        laserRightSeg08 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg08/X/Sensor/Value")
        laserRightSeg09 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg09/X/Sensor/Value")
        laserRightSeg10 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg10/X/Sensor/Value")
        laserRightSeg11 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg11/X/Sensor/Value")
        laserRightSeg12 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg12/X/Sensor/Value")
        laserRightSeg13 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg13/X/Sensor/Value")
        laserRightSeg14 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg14/X/Sensor/Value")
        laserRightSeg15 = device.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg15/X/Sensor/Value")
        return [laserRightSeg01, laserRightSeg02, laserRightSeg03, laserRightSeg04, laserRightSeg05, laserRightSeg06, laserRightSeg07, laserRightSeg08, laserRightSeg09, laserRightSeg10, laserRightSeg11, laserRightSeg12, laserRightSeg13, laserRightSeg14, laserRightSeg15]
    def getLaserFrontGroundLeftRight(self):
        
        device = self.session.service("ALMemory")
        laserGroundFrontRight = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Vertical/Right/Seg01/X/Sensor/Value")
        laserGroundFrontLeft = device.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Vertical/Left/Seg01/X/Sensor/Value")
        return[laserGroundFrontRight, laserGroundFrontLeft]

    """Robotvelocity set functions"""
    def setRobotvelocity(self, x, y, theta):
        motion  = self.session.service("ALMotion")
        motion.move(x, y, theta)
    """Robotvelocity get functions"""
    def getRobotVelocity(self):  
        device = self.session.service("ALMemory")
        speedActuatorFL = device.getData("Device/SubDeviceList/WheelFL/Speed/Actuator/Value")
        speedActuatorFR = device.getData("Device/SubDeviceList/WheelFR/Speed/Actuator/Value")
        speedActuatorB = device.getData("Device/SubDeviceList/WheelB/Speed/Actuator/Value")
        return[speedActuatorFL, speedActuatorFR, speedActuatorB]  #returns speed in (rad/s) of all 3 wheels

    """Head set functions angels"""
    #Head
    def setHeadPitch(self,  angle, speed, isab):
        device = self.session.service("ALMemory")
        HeadYaw = abs(device.getData("Device/SubDeviceList/HeadYaw/Position/Sensor/Value"))
        HeadPitchMax = 3
        HeadPitchMin = 3
        if type(angle) == int or type (angle) == float :
                
                if HeadYaw >= 1.5952 and HeadYaw <= 2.0857:
                    HeadPitchMin = -0.6109
                    HeadPitchMax = 0.2356
                elif HeadYaw >= 1.0751 and HeadYaw <=1.5951 :
                    HeadPitchMin = -0.6109
                    HeadPitchMax = 0.2356
                elif HeadYaw >=0.5817  and HeadYaw <=1.0750 :    
                    HeadPitchMin = -0.6143
                    HeadPitchMax = 0.3647  
                elif HeadYaw >=0  and HeadYaw <=0.5816 :    
                    HeadPitchMin = -0.7068
                    HeadPitchMax = 0.4451  

                if angle >= HeadPitchMin and angle <= HeadPitchMax:
                    motion = self.session.service("ALMotion")
                    names  = ["HeadPitch"]
                    angles = [angle]
                    times  = [speed]
                    isAbsolute = isab
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number! "
    def setHeadYaw(self,  angle, speed, isab):
        if type(angle) == int or type (angle) == float :
                if angle >= -2.0857 and angle <= 2.0857:
                    motion = self.session.service("ALMotion")
                    names  = ["HeadYaw"]
                    angles = [angle]
                    times  = [speed]
                    isAbsolute = isab
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"

    """Head get functions angels"""
    def getHeadYaw(self):
        device = self.session.service("ALMemory")
        HeadYawActor =device.getData("Device/SubDeviceList/HeadYaw/Position/Actuator/Value")
        HeadYawSensor =device.getData("Device/SubDeviceList/HeadYaw/Position/Sensor/Value")
        return [HeadYawActor,HeadYawSensor]
    def getHeadPitch(self):
        device = self.session.service("ALMemory")
        HeadPitchActor =device.getData("Device/SubDeviceList/HeadPitch/Position/Actuator/Value")
        HeadPitchSensor =device.getData("Device/SubDeviceList/HeadPitch/Position/Sensor/Value")
        return [HeadPitchActor,HeadPitchSensor]


    """Left Arm set functions angels"""
    #LeftArm
        #Shoulder
    def setLeftShoulderPitch(self, angle,speed,isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= -2.0857 and angle <= 2.0857:
                    motion = self.session.service("ALMotion")
                    names  = ["LShoulderPitch"]
                    angles = [angle]
                    times  = [speed]
                    
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"
    def setLeftShoulderRoll(self, angle,speed,isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= 0.0087 and angle <= 1.5620:
                    motion = self.session.service("ALMotion")
                    names  = ["LShoulderRoll"]
                    angles = [angle]
                    times  = [speed]
                    
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"
            
    #LeftArm
        #Elbow
    def setLeftElbowYaw(self, angle, speed, isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= -2.0857 and angle <= 2.0857:
                    motion = self.session.service("ALMotion")
                    names  = ["LElbowYaw"]
                    angles = [angle]
                    times  = [speed]
                    
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"    
    def setLeftElbowRoll(self, angle,speed,isAbsolute):
        device = self.session.service("ALMemory")
        if type(angle) == int or type (angle) == float :
                if angle >= -1.5620 and angle <= -0.0087:
                    motion = self.session.service("ALMotion")
                    names  = ["LElbowRoll"]
                    angles = [angle]
                    times  = [speed]
                    
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number! "
        
    #LeftArm
        #Wrist
    def setLeftWristYaw(self, angle,speed,isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= -2.0857 and angle <= 2.0857:
                    motion = self.session.service("ALMotion")
                    names  = ["LWristYaw"]
                    angles = [angle]
                    times  = [speed]
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"

    #LeftArm
         #Hand
    def setLeftHand(self,speed, angle):
        if angle == 0 or angle ==1:
            motion = self.session.service("ALMotion")
            names  = ["LHand"]
            angles = [angle]
            times  = [speed]
            isAbsolute = True
            motion.angleInterpolation(names, angles, times, isAbsolute)

    """Left Arm get functions angels"""
    def getLeftShoulderPitch(self):
        device = self.session.service("ALMemory")
        LeftShoulderPitchActuator =device.getData("Device/SubDeviceList/LShoulderPitch/Position/Actuator/Value")
	LeftShoulderPitchSensor =device.getData("Device/SubDeviceList/LShoulderPitch/Position/Sensor/Value")
        return [LeftShoulderPitchActuator,LeftShoulderPitchSensor]
    def getLeftShoulderRoll(self):
        device = self.session.service("ALMemory")
        LeftShoulderRollActuator =device.getData("Device/SubDeviceList/LShoulderRoll/Position/Actuator/Value")
	LeftShoulderRollSensor =device.getData("Device/SubDeviceList/LShoulderRoll/Position/Sensor/Value")
        return [LeftShoulderRollActuator,LeftShoulderRollSensor]
    def getLeftElbowYaw(self):
        device = self.session.service("ALMemory")
        LeftElbowYawActuator =device.getData("Device/SubDeviceList/LElbowYaw/Position/Actuator/Value")
	LeftElbowYawSensor =device.getData("Device/SubDeviceList/LElbowYaw/Position/Sensor/Value")
        return [LeftElbowYawActuator,LeftElbowYawSensor]
    def getLeftElbowRoll(self):
        device = self.session.service("ALMemory")
        LeftElbowRollActuator =device.getData("Device/SubDeviceList/LElbowRoll/Position/Actuator/Value")
	LeftElbowRollSensor =device.getData("Device/SubDeviceList/LElbowRoll/Position/Sensor/Value")
        return [LeftElbowRollActuator,LeftElbowRollSensor]
    def getLeftWristYaw(self):
        device = self.session.service("ALMemory")
        LeftWristYawActuator =device.getData("Device/SubDeviceList/LWristYaw/Position/Actuator/Value")
	LeftWristYawSensor =device.getData("Device/SubDeviceList/LWristYaw/Position/Sensor/Value")
        return [LeftWristYawActuator,LeftWristYawSensor]

    """ Right Arm set functions angels"""
    #RightArm
        #Shoulder
    def setRightShoulderPitch(self, angle,speed,isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= -2.0857 and angle <= 2.0857:
                    motion = self.session.service("ALMotion")
                    names  = ["RShoulderPitch"]
                    angles = [angle]
                    times  = [speed]
                    
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"
    def setRightShoulderRoll(self, angle,speed,isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= 0.0087 and angle <= 1.5620:
                    motion = self.session.service("ALMotion")
                    names  = ["RShoulderRoll"]
                    angles = [angle]
                    times  = [speed]
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"
            
    #RightArm
        #Elbow
    def setRightElbowYawAbsolute(self, angle,speed, isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= -2.0857 and angle <= 2.0857:
                    motion = self.session.service("ALMotion")
                    names  = ["RElbowYaw"]
                    angles = [angle]
                    times  = [speed]
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"
    
    def setRightElbowRoll(self,angle,speed, isAbsolute):
        device = self.session.service("ALMemory")
        if type(angle) == int or type (angle) == float :
                if angle <= 1.5620 and angle >= 0.0087:
                    motion = self.session.service("ALMotion")
                    names  = ["RElbowRoll"]
                    angles = [angle]
                    times  = [speed]
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number! "
        
    #RightArm
        #Wrist
    def setRightWristYaw(self, angle,speed,isAbsolute):
        if type(angle) == int or type (angle) == float :
                if angle >= -2.0857 and angle <= 2.0857:
                    motion = self.session.service("ALMotion")
                    names  = ["RWristYaw"]
                    angles = [angle]
                    times  = [speed]
                    motion.angleInterpolation(names, angles, times, isAbsolute)
                else:
                    print "No valid angle!"
        else:
            print "The input is not a number!"
    #RightArm
        #Hand
    def setRightHand(self, angle):
        if angle == 0 or angle ==1:
            motion = self.session.service("ALMotion")
            names  = ["RHand"]
            angles = [angle]
            times  = [1.0]
            isAbsolute = True
            motion.angleInterpolation(names, angles, times, isAbsolute)


    """Right Arm get functions angels"""
    def getRightShoulderPitch(self):
        device = self.session.service("ALMemory")
        RightShoulderPitchActuator =device.getData("Device/SubDeviceList/RShoulderPitch/Position/Actuator/Value")
	RightShoulderPitchSensor =device.getData("Device/SubDeviceList/RShoulderPitch/Position/Sensor/Value")
        return [RightShoulderPitchActuator,RightShoulderPitchSensor]
    def getRightShoulderRoll(self):
        device = self.session.service("ALMemory")
        RightShoulderRollActuator =device.getData("Device/SubDeviceList/RShoulderRoll/Position/Actuator/Value")
	RightShoulderRollSensor =device.getData("Device/SubDeviceList/RShoulderRoll/Position/Sensor/Value")
        return [RightShoulderRollActuator,RightShoulderRollSensor]
    def getRightElbowYaw(self):
        device = self.session.service("ALMemory")
        RightElbowYawActuator =device.getData("Device/SubDeviceList/RElbowYaw/Position/Actuator/Value")
	RightElbowYawSensor =device.getData("Device/SubDeviceList/RElbowYaw/Position/Sensor/Value")
        return [RightElbowYawActuator,RightElbowYawSensor]
    def getRightElbowRoll(self):
        device = self.session.service("ALMemory")
        RightElbowRollActuator =device.getData("Device/SubDeviceList/RElbowRoll/Position/Actuator/Value")
	RightElbowRollSensor =device.getData("Device/SubDeviceList/RElbowRoll/Position/Sensor/Value")
        return [RightElbowRollActuator,RightElbowRollSensor]
    def getRightWristYaw(self):
        device = self.session.service("ALMemory")
        RightWristYawActuator =device.getData("Device/SubDeviceList/RWristYaw/Position/Actuator/Value")
	RightWristYawSensor =device.getData("Device/SubDeviceList/RWristYaw/Position/Sensor/Value")
        return [RightWristYawActuator,RightWristYawSensor]

if __name__ == "__main__":

    
    fkt = pepperBasic(ip)

