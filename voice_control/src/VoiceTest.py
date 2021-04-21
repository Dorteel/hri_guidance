#!/usr/bin/env python
import rospy
import intera_interface
import socket
import sys
import time
import random
import errno
import netifaces as ni



rospy.init_node("Voice")
limb = intera_interface.Limb('right')

# Dictionary to comunicate with Sawyer.
rot_dic1 = {'right_j6': 0.0, 'right_j5': 0.0, 'right_j4': 0.0, 'right_j3': 0.0, 'right_j2': 0.0, 'right_j1': 0.0, 'right_j0': 0.0}
rot_dic2 = {'right_j6': 1.0, 'right_j5': 1.0, 'right_j4': 0.0, 'right_j3': 0.0, 'right_j2': 0.0, 'right_j1': 0.0, 'right_j0': 1.0}

# convert the array of floats to the dictionary that Sawyer expect
def values2dic(values):
	global rot_dic
	i = 0
	for j in list(rot_dic.keys())[::-1]:			
		rot_dic[j] = values[i]
		i += 1



##Main Code
try:

	print("-----------------------------")
	print("Unity2Robot")
	print("-----------------------------")
	for i in range(100):
		time.sleep(1)
		if i%2 == 0: 
			limb.move_to_joint_positions(rot_dic1)

		else:
			limb.move_to_joint_positions(rot_dic2)

finally:
	print("Weee did it!")
