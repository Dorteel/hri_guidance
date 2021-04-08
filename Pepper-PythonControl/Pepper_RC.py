import sys, pygame
from naoqi import ALProxy
import qi
import time

ip = "192.168.1.3"
tts = ALProxy("ALTextToSpeech", ip, 9559)
motion = ALProxy("ALMotion", ip, 9559)

#motion.wakeUp()

#motion.setStiffnesses("Body", 1.0)
#motion.moveInit()

#TARGET VELOCITY
X = 0.0
Y = 0.0
Theta = -1
Frequency =1.0 # max speed

#{MaxVelXY, MaxVelTheta, MaxAccXY, MaxAccTheta, MaxJerkXY, MaxJerkTheta, TorsoWy}

#motion.moveToward(X, Y, Theta, [["MaxVelTheta", Frequency], ["MaxAccTheta", Frequency], ["MaxJerkTheta", Frequency]])
X = 0
#motion.moveToward(X, Y, Theta, [["MaxVelXY", Frequency]])
#motion.rest()

pygame.init()
tts.say("I'm walking")
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tts.say("Left Key pressed!")
            if event.key == pygame.K_RIGHT:
                tts.say("Right key pressed!")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                tts.say("Left key released!")
            if event.key == pygame.K_RIGHT:
                tts.say("Right key released!")          


pygame.display.quit()
    
#screen = pygame.display.set_mode(size)
