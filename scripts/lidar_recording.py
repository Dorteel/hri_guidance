#!/usr/bin/env python

from datetime import datetime
import time
import csv
import rospy
from sensor_msgs.msg import LaserScan
import os


dirname = os.path.dirname(__file__)

lidar_ranges = []
lidar_intensities = []

filename = os.path.join(dirname, "..", "Recordings/")
st = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
record_path = filename + str(st) + ".csv"


def callback(data):
    lidar_ranges = data.ranges[:]
    lidar_intensities = data.intensities[:]
    message = [time.time()] + list(lidar_ranges) + list(lidar_intensities)
    record(message, 'a')

def record(torecord, mode):
    file = open(record_path, mode=mode)
    record_writer = csv.writer(file, delimiter=';')#, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    record_writer.writerow(torecord)
    file.close()


def setup_file():
    # Create header
    ranges = ["Range"+ str(x) for x in range(360)]
    intensities = ["Intensity"+ str(x) for x in range(360)]
    header = ["timestamp"] + ranges + intensities
    record(header, 'wb')


def lidar_processing():
    rospy.init_node('lidar_processing', anonymous=True)
    rospy.Subscriber('scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
        setup_file()
        lidar_processing()
        



    
