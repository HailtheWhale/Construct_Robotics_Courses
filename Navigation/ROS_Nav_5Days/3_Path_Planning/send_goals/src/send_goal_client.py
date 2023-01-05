#! /usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def feedback_callback(feedback):
    print('Current Pose is:')
    print('x',feedback.base_position.pose.position.x)
    print('y',feedback.base_position.pose.position.y)
    print('//////////////////')
    # print('The current orientation is:')
    # print('x',feedback.base_position.pose.orientation.x)
    # print('y',feedback.base_position.pose.orientation.y)
    # print('z',feedback.base_position.pose.orientation.z)
    #print('w',feedback.base_position.pose.orientation.w)
    
# initializes the action client node
rospy.init_node('set_goal')

# move_base is the action server
client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
# waits until the action server is up and running
rospy.loginfo('Waiting for action Server ')
client.wait_for_server()
rospy.loginfo('Action Server Found...')

# Setting goal Position function:
def goal_position(truegoal, x_pos, y_pos, x_orient, y_orient, z_orient, w_orient):
    # Target map must be map_frame
    truegoal.target_pose.header.frame_id = 'map'

    truegoal.target_pose.pose.position.x = x_pos
    truegoal.target_pose.pose.position.y = y_pos

    truegoal.target_pose.pose.orientation.x = x_orient
    truegoal.target_pose.pose.orientation.y = y_orient
    truegoal.target_pose.pose.orientation.z = z_orient
    truegoal.target_pose.pose.orientation.w = w_orient
    # Give back updated goal
    return goal

rate = rospy.Rate(1)

while not rospy.is_shutdown():
    # Moving goal object
    goal = MoveBaseGoal()
    goal = goal_position(goal,0.5,0.5,0.0,0.0,0.0,1.0)
    client.send_goal(goal, feedback_cb=feedback_callback)
    rospy.loginfo("Lets Start The Wait for the Action To finish Loop...")
    client.wait_for_result()

    # Moving goal object
    goal = MoveBaseGoal()
    goal = goal_position(goal,-0.5,-3.0,0.0,0.0,0.0,1.0)
    client.send_goal(goal, feedback_cb=feedback_callback)
    rospy.loginfo("Lets Start The Wait for the Action To finish Loop...")
    client.wait_for_result()

    # Moving goal object
    goal = MoveBaseGoal()
    goal = goal_position(goal,1.0,1.0,0.0,0.0,0.0,1.0)
    client.send_goal(goal, feedback_cb=feedback_callback)
    rospy.loginfo("Lets Start The Wait for the Action To finish Loop...")
    client.wait_for_result()

