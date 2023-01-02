#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
from std_srvs.srv import Empty  # you import the service message python classes generated from Empty.srv.
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')

# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/move_bb8_in_circle')

# Create the connection to the service
bb8_circle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

# Execute Service Call
bb8_circle_service()
