import pygame
import math as m


###############
#  H U M A N  #
###############
class Human():
    def __init__(self, humanstyle, pos_x, pos_y):
        self.standingImg = pygame.image.load('images/humans/' + humanstyle + '/standing.png')
        self.walking = [pygame.image.load('images/humans/' + humanstyle + '/walking1.png'), pygame.image.load(
            'images/humans/' + humanstyle + '/walking2.png')]
        self.image = self.standingImg
        self.walkCounter = 0
        self.updateRate = 40
        # Movement State variables
        self.turnLeft = False
        self.turnRight = False
        self.moveForward = False
        self.moveBackward = False
        # Following variables
        self.followDistance = 300
        self.safetyDistance = 20
        # Movement Variables
        self.moveRate = 0
        self.speed = 4
        self.turnRate = 2
        self.angle = 0
        self.x = pos_x
        self.y = pos_y
        # Drawing
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
        self.rotatedImg = None
        self.rotatedRect = None
        # Timing
        # self.timer = pygame.time.get_ticks()

    def rotate(self):
        rotatedImg = pygame.transform.rotozoom(self.image, self.angle, 1)
        rotatedRect = rotatedImg.get_rect(center=(self.x, self.y))
        return (rotatedImg, rotatedRect)

    def update(self, surface):
        if self.moveRate != 0:                                                       # If the character is moving
            if (self.walkCounter % self.updateRate) == 0:                            # If the 40 loops passed
                self.image = self.walking[0]
            elif (self.walkCounter % self.updateRate) == int(self.updateRate/2):
                self.image = self.walking[1]
            self.walkCounter += 1
        else:
            self.image = self.standingImg
            #self.walkCounter = 0

        self.rotatedImg, self.rotatedRect = self.rotate()
        surface.blit(self.rotatedImg, self.rotatedRect)

    def calculatePosition(self):
        # based on angle, get x and y component
        # Limit angle to 360 range
        self.angle = self.angle % 360
        x_comp = -m.sin(m.radians(self.angle))
        y_comp = -m.cos(m.radians(self.angle))

        self.x += int(x_comp*self.moveRate)
        self.y += int(y_comp * self.moveRate)

    def turnTowards(self, object):
        x_diff = object.x - self.x
        y_diff = object.y - self.y
        self.angle = 270 + m.degrees(m.atan2(-y_diff, x_diff))

    def follow(self, object):
        self.turnTowards(object)
        distance = m.sqrt((object.x - self.x)**2 + (object.y - self.y)**2)
        if distance > self.followDistance: # and distance > self.safetyDistance:
            self.moveForward = True
        else:
            self.moveForward = False

    def move(self):
        if self.turnRight and not self.turnLeft:
            self.angle -= self.turnRate
        elif not self.turnRight and self.turnLeft:
            self.angle += self.turnRate

        if self.moveForward and not self.moveBackward:
            self.moveRate = self.speed
        elif not self.moveForward and self.moveBackward:
            self.moveRate = -self.speed
        else:
            self.moveRate = 0
        self.calculatePosition()

###############
#  R O B O T  #
###############
class Robot():
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load('images/Pepper.png')
        # Movement State variables
        self.turnLeft = False
        self.turnRight = False
        self.moveForward = False
        self.moveBackward = False
        # Movement Variables
        self.moveRate = 0
        self.speed = 5
        self.turnRate = 2
        self.angle = 0
        self.x = pos_x
        self.y = pos_y
        # Drawing
        self.rect = self.image.get_rect()
        self.rotatedImg = None
        self.rotatedRect = None

    def rotate(self):
        rotatedImg = pygame.transform.rotozoom(self.image, self.angle, 1)
        rotatedRect = rotatedImg.get_rect(center=(self.x, self.y))
        return (rotatedImg, rotatedRect)

    def update(self, surface):
        self.rotatedImg, self.rotatedRect = self.rotate()
        surface.blit(self.rotatedImg, self.rotatedRect)

    def calculatePosition(self):
        # based on angle, get x and y component
        # Limit angle to 360 range
        self.angle = self.angle % 360
        x_comp = -m.sin(m.radians(self.angle))
        y_comp = -m.cos(m.radians(self.angle))

        self.x += int(x_comp * self.moveRate)
        self.y += int(y_comp * self.moveRate)

    def move(self):
        if self.turnRight and not self.turnLeft:
            self.angle -= self.turnRate
        elif not self.turnRight and self.turnLeft:
            self.angle += self.turnRate

        if self.moveForward and not self.moveBackward:
            self.moveRate = self.speed
        elif not self.moveForward and self.moveBackward:
            self.moveRate = -self.speed
        else:
            self.moveRate = 0
        self.calculatePosition()