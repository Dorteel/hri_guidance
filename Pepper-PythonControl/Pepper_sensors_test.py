#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use getData Method to Get Inertial Values"""

import qi
import argparse
import sys
import pepper_keys

ip = "192.168.1.3"

def laser_transform(lasers):
    pass
        

def main(session):
    """
    This example uses the getData method to get Inertial Values.
    """
    # Get the service ALMemory.
    lasers = pepper_keys.laser_keys
    memory_service = session.service("ALMemory")

    # Get the Laser Values
    laser_values = memory_service.getListData(lasers)    
    #print(laser_values)

    laser_xy= [round(num*100) for num in laser_values]

    laser_right_xy = list(zip(laser_xy[:15],laser_xy[15:30]))
    laser_front_xy = list(zip(laser_xy[30:45],laser_xy[45:60]))
    laser_left_xy = list(zip(laser_xy[60:75],laser_xy[75:90]))
    print (laser_right_xy)
    print('-----')
    print (laser_front_xy)
    print(laser_right_xy[0][0])
    print(laser_right_xy[0][1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default= ip,
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.1.3'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)

# WORKING
# HeadYaw
# Device/SubDeviceList/HeadYaw/Position/Actuator/Value
# 
# Device/SubDeviceList/LElbowRoll/Position/Sensor/Value
