#! /usr/bin/env python

import rospy
# Velocity and LaserScan message types  
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# Define global variable at max distance
# This will allow access of data from the subscriber. 
scan_front = 30
scan_right = 30
scan_left = 30

# Runs when sub runs
def callback(msg):
    scan = msg.ranges
    # Add global variables 
    global scan_front
    global scan_right
    global scan_left
    # Redefine these variables 
    scan_front = scan[360]
    scan_left = scan[719]
    scan_right = scan[0]


# Initiate a Node 
rospy.init_node('sub_pub_quiz_node')
# Create a Publisher object to the /cmd_vel topic to make bot move. 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    
# Make Subscriber Object 
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)  

# Make Twist msg 
move = Twist()

# Initializing the Movement...
move.linear.x = 0
move.angular.z = 0

# Set a publish rate of 2 Hz
rate = rospy.Rate(2)

# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
  # Wall in front farther than 1 m, do checks 
  if (scan_front > 1):
    # If left close, turn right 
    if (scan_left < 1):
        move.linear.x = 0
        move.angular.z = -0.8
    # If right close, turn left 
    elif (scan_right < 1):
        move.linear.x = 0
        move.angular.z = 0.8
    # Else, move forward.
    else:
        move.linear.x = 0.4
        move.angular.z = 0
  # Wall closer than 1 m, turn left. 
  else:
    move.linear.x = 0
    move.angular.z = 0.8
  # Publish the message within the 'move' variable
  pub.publish(move)
  # Make sure the publish rate maintains at 2 Hz
  rate.sleep()                             