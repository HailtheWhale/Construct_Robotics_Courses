#! /usr/bin/env python
import rospy
# Import the service message used by the service /trajectory_by_name
from std_srvs.srv import Empty  # you import the service message python classes generated from Empty.srv.

# Initialise a ROS node with the name service_client
rospy.init_node('init_particles_service_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/global_localization')
# Create the connection to the service
init_particles_service = rospy.ServiceProxy('/global_localization', Empty)
# Execute Service Call
init_particles_service()