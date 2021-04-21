#!/usr/bin/env python
import rospy
import intera_interface
import socket
import sys
import time
import random
import errno
import netifaces as ni

from pocketsphinx import LiveSpeech


rospy.init_node("Voice")
limb = intera_interface.Limb('right')

# Dictionary to comunicate with Sawyer.
rot_dic1 = {'right_j6': 0.0, 'right_j5': 0.0, 'right_j4': 0.0, 'right_j3': 0.0, 'right_j2': 0.0, 'right_j1': 0.0, 'right_j0': 0.0}
rot_dic2 = {'right_j6': 0.0, 'right_j5': 0.0, 'right_j4': 0.0, 'right_j3': 0.0, 'right_j2': 0.0, 'right_j1': 0.0, 'right_j0': 1.0}


def parseVoice(word):
	if 'go' and 'left' in word:
		print('Moving left...')
		limb.move_to_joint_positions(rot_dic2)
	if 'go' and 'right' in word:
		print('Moving right...')
		limb.move_to_joint_positions(rot_dic1)
	if 'go' and 'up' in word:
		print('Moving up...')
	if 'go' and 'down' in word:
		print('Moving down...')

def exitCondition(word):
	if 'exit' or 'quit' in word:
		return True
	return False


##Main Code
print("-----------------------------")
print("Unity2Robot")
print("-----------------------------")

speech = LiveSpeech(lm=False, kws='/home/student/ros_ws/src/voice_control/src/key.list', verbose=False, no_search=False, full_utt=False, buffer_size=1048, sampling_rate=16000)
exit = False

while not exit:
	for phrase in speech:
		word = str(phrase)
		parseVoice(word)
		exit = exitCondition(word)
		#if exit: break
			
	
