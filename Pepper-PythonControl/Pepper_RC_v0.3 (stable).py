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

def drawBackground():
    screen.fill(black)
    # Draw a rectangle - coordinates for top left of the object
    #   Height and Width of rectangle
    recH = round(height/3*2)
    recW = round(width/3*2)
    #   X, Y coordinates
    recX = round((width - recW)/2)
    recY = round((height - recH)/2)
    #   Draw the rectangle
    #pygame.draw.rect(screen, white, [recX, recY, recW, recH ])
    
    pygame.draw.circle(screen, white, (int(midX), int(midY)), radius)
    #   Draw a black dot representing Pepper
    pygame.draw.rect(screen, black, [midX, midY, 10, 10 ])

pygame.init()

button_keys = {"left_stick_click": 7, "right_stick_click": 8, "PS": 5}

joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

turnLeft = False
turnRight = False
moveForward = False
moveBackward = False

size = width, height = 1280, 720
radius = int(min([width, height])/2)

midX, midY = round(width/2), round(height/2)
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

maxRange = 0
pygame.display.set_caption('Pepper Remote Control')
running = True

# Get the service ALMemory.
lasers = pepper_keys.laser_keys
#memory_service = session.service("ALMemory")

##################################### ANALOG INPUTS ###############################
# LEFT JOYSTICK
# analog_keys[0] left: -1, right: 1
# analog_keys[1] down: 1, up: -1

# RIGHT JOYSTICK
# analog_keys[2] left: -1, right: 1
# analog_keys[3] down: 1, up: -1
analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1}

while running:
    drawBackground()
    #xVel, yVel, thetaVel = 0, 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            yVel = -round(analog_keys[0],2) if abs(analog_keys[0]) > .2 else 0
            xVel = -round(analog_keys[1],2) if abs(analog_keys[1]) > .2 else 0
            thetaVel = -round(analog_keys[2],2) if abs(analog_keys[2]) > .2 else 0

    move(xVel,yVel,thetaVel)       

    # Get the Sonar Values
    sonar_value_front = memory.getData("Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
    sonar_value_back = memory.getData("Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value")
    #print("Front: " + str(sonar_value_front) + "Back: " + str(sonar_value_back))
    # Draw the sonar values
    pygame.draw.rect(screen, blue, [midX-20, midY-(sonar_value_front*(radius/6.5)), 50, 5])         # Front sonar
    pygame.draw.rect(screen, blue, [midX-20, midY+(sonar_value_back*(radius/6.5)), 50, 5])         # Back sonar

    # Get the Laser Values
    laser_values = memory.getListData(lasers)
    maxRange = max(laser_values) if max(laser_values) > maxRange else maxRange

    
    # Transform coordinates to pixel values
    laser_xy= [round(num*round((radius)/7)) for num in laser_values]

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

