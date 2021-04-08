import sys, pygame, math
from naoqi import ALProxy
import qi
import time
import threading
import pepper_keys

# Make sure you're connected to the same network as Pepper!
ip = "192.168.1.3"
tts = ALProxy("ALTextToSpeech", ip, 9559)
motion = ALProxy("ALMotion", ip, 9559)
memory = ALProxy("ALMemory", ip, 9559)

#TARGET VELOCITY
X = 1.0
Y = 0.0
theta = -1
Frequency =1.0 # max speed

def move(X, Y, Theta):
    #motion.post.moveToward(X, Y, Theta, [["MaxVelTheta", Frequency],
    #["MaxAccTheta", Frequency], ["MaxJerkTheta", Frequency]])
    motion.post.moveToward(X, Y, Theta)



pygame.init()

turnLeft = False
turnRight = False
moveForward = False
moveBackward = False

size = width, height = 1280, 1280

midX, midY = round(width/2), round(height/2)
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen.fill(black)

pygame.display.set_caption('Pepper Remote Control')
running = True

# Get the service ALMemory.
lasers = pepper_keys.laser_keys
#memory_service = session.service("ALMemory")

# Draw a rectangle - coordinates for top left of the object
#   Height and Width of rectangle
recH = round(height/3*2)
recW = round(width/3*2)
#   X, Y coordinates
recX = round((width - recW)/2)
recY = round((height - recH)/2)

#   Draw the rectangle
pygame.draw.rect(screen, white, [recX, recY, recW, recH ])

#   Draw a black dot representing Pepper
pygame.draw.rect(screen, black, [midX, midY, 10, 10 ])

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
    elif turnRight and not turnLeft and not moveForward and moveBackward:
        move(-X, 0, -theta)
    elif not turnRight and turnLeft and moveForward and not moveBackward:
        move(X, 0, -theta)
    elif not turnRight and turnLeft and not moveForward and moveBackward:
        move(-X, 0, theta)
    elif not turnRight and not turnLeft and moveForward and not moveBackward:
        move(X, 0, 0)
    elif not turnRight and not turnLeft and not moveForward and moveBackward:
        move(-X, 0, 0)
    else:
        move(0,0,0)

    # Get the Laser Values
    laser_values = memory.getListData(lasers)
    # Transform coordinates to pixel values
    laser_xy= [round(num*100) for num in laser_values]

    laser_right_xy = list(zip(laser_xy[:15],laser_xy[15:30]))
    laser_front_xy = list(zip(laser_xy[30:45],laser_xy[45:60]))
    laser_left_xy = list(zip(laser_xy[60:75],laser_xy[75:90]))
    
    lasers_all = laser_right_xy + laser_front_xy + laser_left_xy

    # Draw a rectangle for each coordinate
    for xy in laser_right_xy:
        x = midX + xy[0]
        y = midY - xy[1]
        pygame.draw.rect(screen, red, [x, y, 5, 5])
    for xy in laser_front_xy:
        x = midX - xy[1]
        y = midY - xy[0] 
        pygame.draw.rect(screen, red, [x, y, 5, 5])
    for xy in laser_left_xy:
        x = midX - xy[0]
        y = midY + xy[1] 
        pygame.draw.rect(screen, red, [x, y, 5, 5])
    
    
    # Update the screen
    pygame.display.update()
pygame.display.quit()

