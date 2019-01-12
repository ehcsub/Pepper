## @package pepperConnect
#  Documentation for this module.
#  this module handels connection to pepper.
#  More details.

import qi
import argparse
import sys
import time
import random

## Documentation for the pepperConnect Class.
#
#  More details.
class pepperConnect():
    
    ## The constructor.
    #  @param self The object pointer.
    #  @param ip address.
    def __init__(self,ip):
    
        self.ipAddress= ip
        self.session = qi.Session()
        self.connectToRobot()

    ## this function connects to the Robot.
    #  @param self The object pointer.
    def connectToRobot(self):

        ip=self.ipAddress
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default=ip,
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
        parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
        args = parser.parse_args()
        try:
            self.session.connect("tcp://" + args.ip + ":" + str(args.port))
            print "pepperConnect"
            print "connected to: ",self.ipAddress
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
                "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

if __name__ == "__main__":

    fkt = pepperConnect("10.95.249.12")  


