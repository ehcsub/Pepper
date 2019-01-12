import qi
import argparse
import sys
import time
import datetime
from naoqi import ALProxy
from pepperConnect import pepperConnect

ip = "10.95.249.12"
#ip = "192.168.178.24"


fkt = pepperConnect(ip)
session = fkt.session

posture_service = session.service("ALRobotPosture")
life_service = session.service("ALAutonomousLife")

life_service.setAutonomousAbilityEnabled("BasicAwareness", False)
life_service.setAutonomousAbilityEnabled("BackgroundMovement", False)
posture_service.goToPosture("StandInit", 2)

print "disabled: BasicAwareness and BackgroundMovement      Ready to go!"
