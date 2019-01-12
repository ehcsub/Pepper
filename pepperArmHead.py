## @package pepperArmHead
#  Documentation for this module.
#
#  More details.

import qi
import argparse
import sys
import time
import random
from pepperGenerall import pepperGenerall
from pepperConnect import pepperConnect




## Documentation for pepperArmHead Class.
#
#  More details.
class pepperArmHead(pepperConnect):

    ## the constructor.
    #  @param self	 the object pointer.
    #  @param name 	name of the object.
    #  @param headPosition int	 	0-3 selection of the workspace 0=topLeft 3=bottomRight .
    #  @param cornerArmPositions	 List with the Corners of the 4 workspaces[  [[ws0,ws0],[ws0,ws0],[ws0,ws0],[ws0,ws0]]   ,   [[ws1,ws1],[ws1,ws1],[ws1,ws1],[ws1,ws1]]  ,   [[ws2,ws2],[ws2,ws2],[ws2,ws2],[ws2,ws2]]   ,   [[ws3,ws3],[ws3,ws3],[ws3,ws3],[ws3,ws3]]  ] .
    #  @param arm int	select the are for the workspace 1=leftArm 0=rightArm.
    #  @param headWorkSpace	 list with the angles,for the initial headpositions, for the 4 workspaces.[[ws0,ws0],[ws1,ws1],[ws2,ws2],[ws3,ws3]]
    #  @param ip	 Ip adress of the pepper robot.
    def __init__(self ,name,headPosition,cornerArmPositions, arm, headWorkSpace,ip):
        
        self.name=name
        self.headPosition=headPosition             #Head position 0 oben links 1 unten links 2 oben rechts 3 unten rechts
        self.armUsed = arm                        #selected Arm 1=left 0=right 
        self.cornerArmPosition=cornerArmPositions  #roll and pitch of shoulder for corner position
        self.headWorkSpace= headWorkSpace          #Yaw and pitch of the 4 Workspaces [0]links oben...[3]rechts unten
        self.ipAddress = ip
        self.session = qi.Session()
        self.connectToRobot()
        self.pepperGenerall = pepperGenerall(ip,self.session)

            
    ## This function moves the choosen arm to a random position in the given workspace.
    #
    #  More details.
    def moveArmToRandomPosition(self):

        pitchRollAngle = [0,0]
        pitchList = []
        rollList =[]
        for i in range (0,4):
            pitchList.append(self.cornerArmPosition[self.headPosition][i][0])
            rollList.append((self.cornerArmPosition[self.headPosition][i][1]))
        
        pitchMax=max(pitchList)
        pitchMin=min(pitchList)
        rollMax=max(rollList)
        rollMin=min(rollList)
        pitchRollAngle[0] = round(random.uniform(pitchMax,pitchMin), 3)
        pitchRollAngle[1] = round(random.uniform(rollMax,rollMin),3)   
        print pitchList
        print rollList
        print pitchRollAngle

        if self.armUsed==1:
            succes = self.pepperGenerall.setLeftArm(pitchRollAngle)
        else:
            succes = self.pepperGenerall.setRightArm(pitchRollAngle)

        return succes

    ## This function returns the curren headYaw and headPitch angles in a list with 2 elements.
    #
    #  More details.
    def getCurrentHeadPosition(self):

        hp = [0,0]
        i = self.pepperGenerall.pepperBasic.getHeadYaw()
        r = self.pepperGenerall.pepperBasic.getHeadPitch()
        hp[0] = round(i[1],3)
        hp[1] = round(r[1],3)
        return hp
    
    ## This function returns the current ShoulderPitch and ShoulderRoll in a list with 2 elements. 
    #
    #  More details.
    def getCurrentArmPosition(self):

        if self.armUsed ==1:
            ap=[0,0]
            i = self.pepperGenerall.pepperBasic.getLeftShoulderPitch()
            r = self.pepperGenerall.pepperBasic.getLeftShoulderRoll()
            ap[0]=round(i[1],3)
            ap[1]=round(r[1],3)
            return ap

        else:
            ap=[0,0]
            i = self.pepperGenerall.pepperBasic.getRightShoulderPitch()
            r = self.pepperGenerall.pepperBasic.getRightShoulderRoll()
            ap[0]=round(i[1],3)
            ap[1]=round(r[1],3)
            return ap            
    
    ## This function moves the Head to the inital position of the given workspace.
    #
    #  More details.
    def setHeadPositionWorkSpace(self):
        return self.pepperGenerall.setHead(self.headWorkSpace[self.headPosition])
    
    ## This function sets the arm to the given angles
    #  @param angle list of 2 float elements
    #  @param isAbsolute 1 for True and 0 for False   
    #  @param armToMove is only needed if you want to move both arms 1=leftArm---0=rightArm
    #  More details.
    def setArmPosition(self, angle, isAbsolute,armToMove=None):
        if armToMove:
            if self.armUsed==1:
                return self.pepperGenerall.setLeftArm(angle, isAbsolute)
            else:
                return self.pepperGenerall.setRightArm(angle, isAbsolute)
        else:
            if armToMove== 1:
                self.pepperGenerall.setLeftArm(angle, isAbsolute,)
            else:
                self.pepperGenerall.setRightArm(angle, isAbsolute)


    
