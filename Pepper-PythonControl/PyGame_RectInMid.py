import sys, pygame
from naoqi import ALProxy
import qi
import time
import threading

# Make sure you're connected to the same network as Pepper!


#TARGET VELOCITY
X = 1.0
Y = 0.0
theta = -1
Frequency =1.0 # max speed

def move(X, Y, Theta):

    pass

pygame.init()

turnLeft = False
turnRight = False
moveForward = False
moveBackward = False

size = width, height = 600, 600
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen.fill(black)

pygame.display.set_caption('Pepper Remote Control')
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

    # Draw a rectangle - coordinates for top left of the object
    #   Height and Width of rectangle
    recH = round(height/3*2)
    recW = round(width/3*2)
    #   X, Y coordinates
    recX = round((width - recW)/2)
    recY = round((height - recH)/2)

    #   Draw the rectangle
    pygame.draw.rect(screen, white, [recX, recY, recW, recH ])
                     
    # Update the screen
    pygame.display.update()
pygame.display.quit()

