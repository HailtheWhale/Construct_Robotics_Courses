#! /usr/bin/env python
import rospy
from nav_msgs.srv import GetPlan, GetPlanRequest

# Initialise a ROS node with the name service_client
rospy.init_node('get_plan_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/move_base/make_plan')
# Create the connection to the service
get_plan_client = rospy.ServiceProxy('/move_base/make_plan', GetPlan)
# Make the service call msg 
msg = GetPlanRequest()
msg.start.header.frame_id='map'
msg.goal.header.frame_id = 'map'
msg.goal.pose.position.x=1.16
msg.goal.pose.position.y=-4.5
msg.goal.pose.orientation.z=0.75
msg.goal.pose.orientation.w=0.66

# Execute Service Call
get_plan_client(msg)

