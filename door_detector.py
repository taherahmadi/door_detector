#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import math
from time import time

from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan

from sensor_msgs.msg import Image


class robot_control:

  def __init__(self):
    self.move_pub = rospy.Publisher('/komodo_1/diff_driver/command', Twist, queue_size = 1)
    rospy.init_node('talker')
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/komodo_1/Asus_Camera/rgb/image_raw",Image,self.callback)
    rospy.Subscriber('/komodo_1/scan', LaserScan, self.check_distance)
    self.red_lintel_found = False
    self.current_distance = 30.0
    self.length1 = 0.0
    self.length2 = 0.0
    self.colorCounter = 0
    self.sawGreen = False
    self.sawRed = False
    self.sawBlue = False
    self.msg = Twist()

  def stop(self):
    self.msg.linear.x = 0.0
    self.msg.angular.z = 0.0
    self.move_pub.publish(self.msg)
    rospy.sleep(1.0)

  def calculate_forward_angle(self):
    if(self.colorCounter == 1):
      return -0.1

    if(self.colorCounter == 2):
      return -0.01
      
    if(self.colorCounter == 3):
      return 0.04


  def move_forward(self):
    self.msg.linear.x = 1.0
    self.msg.angular.z = self.calculate_forward_angle()
    self.move_pub.publish(self.msg)
    while(self.current_distance > 3.0):
      self.msg.linear.x = 1.0
    self.stop()
    if self.colorCounter == 1:
      self.msg.angular.z = 0.75
    if self.colorCounter == 2:
      self.msg.angular.z = -0.25
    if self.colorCounter == 3:
      self.msg.angular.z = -0.75
    self.msg.linear.x = 1.0
    self.move_pub.publish(self.msg)
    if self.colorCounter == 3:
      rospy.sleep(1.0)
      print "last change"
      self.msg.angular.z = 0.22
      self.move_pub.publish(self.msg)
    if self.colorCounter == 1:
      rospy.sleep(1.0)
      print "last change"
      self.msg.angular.z = -0.5
      self.move_pub.publish(self.msg)


  def moveRobot(self):
    while not self.red_lintel_found:
      self.msg.angular.z = -2.0
      self.move_pub.publish(self.msg)
      rospy.sleep(0.3)
      self.stop()
    print "after first while"
    self.move_forward()


  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    (rows,cols,channels) = cv_image.shape
    red = False
    blue = False
    green = False
    for x in range((rows/2)-20, (rows/2)+20):
      for y in range((cols/2)-20, (cols/2)+20):
        if(cv_image[x,y,0] <= 5 and cv_image[x,y,1] <= 5 and cv_image[x,y,2] >= 100):
          red = True
          if(self.sawRed == False):
            self.colorCounter = self.colorCounter + 1
            self.sawRed = True
          break
        if(cv_image[x,y,0] >= 100 and cv_image[x,y,1] <= 5 and cv_image[x,y,2] <= 5):
          blue = True
          if(self.sawBlue == False):
            self.colorCounter = self.colorCounter + 1
            self.sawBlue = True
          break
        if(cv_image[x,y,0] <= 5 and cv_image[x,y,1] >= 100 and cv_image[x,y,2] <= 5):
          green = True
          if(self.sawGreen == False):
            self.colorCounter = self.colorCounter + 1
            self.sawGreen = True
          break
        #print str(cv_image[x,y,0]) + " " + str(cv_image[x,y,1]) + " " + str(cv_image[x,y,2])
    if(green):
    	print "green!"

    if(red):
    	self.red_lintel_found = True
    	print "red!"

    if(blue):
    	print "blue!"
    
  def check_distance(self, laser_data):
    laser_rays_count = len(laser_data.ranges)
    middle_ray = laser_rays_count / 2
    self.current_distance = laser_data.ranges[middle_ray]
    print "The distance is: %0.1f" % self.current_distance

def main(args):
  # Movement
  rc = robot_control()
  rc.moveRobot()

if __name__ == '__main__':
    main(sys.argv)

