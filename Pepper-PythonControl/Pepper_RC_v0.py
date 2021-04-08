import sys, pygame
from naoqi import ALProxy
import qi
import time
import threading

ip = "192.168.1.3"
tts = ALProxy("ALTextToSpeech", ip, 9559)
motion = ALProxy("ALMotion", ip, 9559)

#TARGET VELOCITY
X = 1.0
Y = 0.0
theta = -1
Frequency =1.0 # max speed

def move(X, Y, Theta):
    #motion.post.moveToward(X, Y, Theta, [["MaxVelTheta", Frequency], ["MaxAccTheta", Frequency], ["MaxJerkTheta", Frequency]])
    motion.post.moveToward(X, Y, Theta)

pygame.init()

turnLeft = False
turnRight = False
moveForward = False
moveBackward = False

size = width, height = 1080, 1080
screen = pygame.display.set_mode(size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left Key pressed!")
                turnLeft = True
            if event.key == pygame.K_RIGHT:
                print("Right key pressed!")
                turnRight = True
            if event.key == pygame.K_UP:
                print("Up key pressed!")
                moveForward = True
            if event.key == pygame.K_DOWN:
                print("Down key pressed!")
                moveBackward = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("Left key released!")
                turnLeft = False
            if event.key == pygame.K_RIGHT:
                print("Right key released!")
                turnRight = False
            if event.key == pygame.K_UP:
                print("Up key released!")
                moveForward = False
            if event.key == pygame.K_DOWN:
                print("Down key released!")
                moveBackward = False
                
    if turnRight and not turnLeft and not moveForward and not moveBackward:
        move(0, 0, theta)
    elif not turnRight and turnLeft and not moveForward and not moveBackward:
        move(0, 0, -theta)
    elif turnRight and not turnLeft and moveForward and not moveBackward:
        move(X, 0, theta)
    elif turnRight and turnLeft and not moveForward and moveBackward:
        move(-X, 0, theta)
    elif not turnRight and turnLeft and moveForward and not moveBackward:
        move(X, 0, -theta)
    elif not turnRight and turnLeft and not moveForward and moveBackward:
        move(-X, 0, -theta)
    elif not turnRight and not turnLeft and moveForward and not moveBackward:
        move(X, 0, 0)
    elif not turnRight and not turnLeft and not moveForward and moveBackward:
        move(-X, 0, 0)
    else:
        move(0,0,0)


pygame.display.quit()

