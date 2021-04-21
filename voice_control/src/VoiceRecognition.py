#!/usr/bin/env python
from pocketsphinx import LiveSpeech


speech = LiveSpeech(lm=False, kws='/home/student/ros_ws/src/voice_control/src/key.list', verbose=False, no_search=False, full_utt=False, buffer_size=1048, sampling_rate=16000)

def parseVoice(word):
    if 'go' and 'left' in word:
	print('Moving left...')
    if 'move' in word:
	print('Stopping...')
    if 'move' and 'up' in word:
	print('Moving up...')
    if 'exit' in word:
	return -2
    return 1

for phrase in speech:
    word = str(phrase)
    if parseVoice(word) == -1:
	break
    if parseVoice(word) == -2:
	quit




