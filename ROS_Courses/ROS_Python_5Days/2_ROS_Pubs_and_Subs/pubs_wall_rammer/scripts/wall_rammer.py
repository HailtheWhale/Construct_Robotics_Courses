#! /usr/bin/env python

# To control timings
import time
# Import the Python library for ROS
import rospy
# Import the Twist message from the geometry_msgs package
from geometry_msgs.msg import Twist


# Initiate a Node named 'topic_publisher'
rospy.init_node('wall_rammer')

# Create a Publisher object to the /cmd_vel topic to make bot move. 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    
                                           
# Set a publish rate of 200 Hz
rate = rospy.Rate(200)
# Create a variable of type Twist. 
# Foundd via "rostopic info /cmd_vel"
move = Twist()
# Setting the different parameters
# Found via "rosmsg show geometry_msgs/Twist"
move.linear.x = 0
move.angular.z = 0

# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
    i = 1
    # Infinite loop
    while (i == 1):
        # Move Fast 
        move.linear.x = 0.6
        move.angular.z = 0
        # Publish movement cmds
        pub.publish(move)
        time.sleep(2)

        # Reverse!
        move.linear.x = -0.3
        move.angular.z = 0
        # Publish Movement Commands
        pub.publish(move)
        time.sleep(2)

        # Movie Reference
        print("Your floor is now clean!")
        
        # Make sure the publish rate maintains at 200 Hz
        rate.sleep()  
        # Stop looping if shutdown.
        if (rospy.is_shutdown()):
            break                       