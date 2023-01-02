#! /usr/bin/env python

import rospy                                          
from exercise_33.msg import Age

# Make node 
rospy.init_node('Age_Pub')                   
pub = rospy.Publisher('/age', Age, queue_size=1)  

# Set a publish rate of 2 Hz
rate = rospy.Rate(2)

# Make age msg
age = Age()
age.years = 42
age.months = 3 
age.days = 1

# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
  # Publish the message within the 'move' variable
  pub.publish(age)
  # Make sure the publish rate maintains at 2 Hz
  rate.sleep()                                         