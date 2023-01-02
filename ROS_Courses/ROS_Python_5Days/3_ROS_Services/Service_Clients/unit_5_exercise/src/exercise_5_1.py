#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
from iri_wam_reproduce_trajectory.srv import ExecTraj
import sys
import rospkg

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')

# Create the connection to the service
exec_traj_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)

# Defining the input to the Service Call
rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

# Send through the connection the name of the trajectory to be executed by the robot
result = exec_traj_service(traj)
# Print the result given by the service called
print(result)