#! /usr/bin/env python

import rospy
# Import the service messages
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('bb8_service_client')

# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/move_bb8_in_circle_custom')

# Create the connection to the service
bb8_circle_service_custom = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

# Execute Service Call
bb8_circle_service_custom(3)