from naoqi import ALProxy
import qi
import time

ip = "192.168.1.3"
tts = ALProxy("ALTextToSpeech", ip, 9559)
motion = ALProxy("ALMotion", ip, 9559)

#motion.wakeUp()

motion.setStiffnesses("Body", 1.0)
motion.moveInit()

#TARGET VELOCITY
X = 0.0
Y = 0.0
Theta = -1
Frequency =1.0 # max speed

#{MaxVelXY, MaxVelTheta, MaxAccXY, MaxAccTheta, MaxJerkXY, MaxJerkTheta, TorsoWy}

motion.moveToward(X, Y, Theta, [["MaxVelTheta", Frequency], ["MaxAccTheta", Frequency], ["MaxJerkTheta", Frequency]])
X = 0
#motion.moveToward(X, Y, Theta, [["MaxVelXY", Frequency]])
#motion.rest()
