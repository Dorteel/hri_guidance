#!/usr/bin/env python

import pygame
import rospy
from sensor_msgs.msg import LaserScan
from numpy import inf
import math

lidar_readings = []
window_w = 1024
window_h = 1024
# lidar range in meters
lrange = 16
# Additional scaling
scaling = 2
# scale the laser cloud
scale = (window_w+window_h)/lrange/2 * scaling

mid_h = int(window_h/2)
mid_w = int(window_w/2)
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
angle_increment = 0.01745329252

def callback(data):
    lidar_readings =[x if x != inf else 0 for x in data.ranges]
    visualize(lidar_readings)

def screen_reset():
    # Fill the screen with white
    screen.fill(white)
    # Draw a black circle
    pygame.draw.circle(screen, black, (mid_w, mid_h), 5)

def setup_visuals():
    # Initilize game
    pygame.init()
    # Set up the drawing window
    global screen 
    screen = pygame.display.set_mode([window_w, window_h])
    # Fill the background with white
    screen.fill(white)
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, black, (mid_w, mid_h), 10)

def visualize(readings):
    screen_reset()
    for deg in range(len(readings)):
        val = readings[deg]*scale
        rads = deg*angle_increment
        # X and Y coordinate differences as seen from center
        d_y = int(val*math.cos(rads))
        d_x = int(val*math.sin(rads))
        x = mid_h - d_x
        y = mid_w - d_y
        # Draw the circle
        pygame.draw.circle(screen, red, (x, y), 3)

    pygame.display.flip()

def lidar_processing():
    setup_visuals()
    rospy.init_node('lidar_processing', anonymous=True)
    rospy.Subscriber('scan', LaserScan, callback)
    rospy.spin()





if __name__ == '__main__':
        lidar_processing()
        



    
