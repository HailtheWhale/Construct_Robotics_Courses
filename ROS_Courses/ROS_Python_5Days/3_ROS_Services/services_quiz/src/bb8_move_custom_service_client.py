#! /usr/bin/env python

import rospy
# Import the service messages
from services_quiz.srv import BB8CustomServiceMessage
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('bb8_service_client')

# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/move_bb8_in_square_custom')

# Create the connection to the service
bb8_square_service_custom = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)

# Execute Service Call: SMALL square TWICE. 
bb8_square_service_custom(0.5,2)
# Execute Service Call: BIG square ONCE.
bb8_square_service_custom(1.5,1)