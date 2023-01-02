#! /usr/bin/env python

import time
import rospy
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
# Add twist cmds for movement 
from geometry_msgs.msg import Twist

# Add Goal State Constants 
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4
# Start img counter
nImage = 1

# Feedback loop
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# initializes the action client node
rospy.init_node('drone_action_client')

# Initialize publisher 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

# create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 20 

# sends the goal to the action server
client.send_goal(goal, feedback_cb=feedback_callback)

# To retrieve state of action without waiting 
state_result = client.get_state()
rate = rospy.Rate(1)

# To continuously update the user with the state info
rospy.loginfo("state_result: "+str(state_result))

if state_result < DONE:
    # Initializing twist movements 
    move = Twist()
    move.linear.x = 0
    move.linear.y = 0
    move.linear.z = 1
    move.angular.x = 0
    move.angular.y = 0
    move.angular.z = 0

    # To ensure that it publishes takeoff
    for i in range(0,5):
        # Move
        pub.publish(move)
        # Wait until in the air
        time.sleep(1)

# While the drone is still taking images 
while state_result < DONE:
    # Change the velocity commands so that the drone flies in a circle
    move.linear.x = 2
    move.linear.y = 0
    move.linear.z = 0
    move.angular.z = 0.8
    pub.publish(move)
    # Do the rest of the things
    rate.sleep()
    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result))

# Provide extra info about the state    
rospy.loginfo("[Result] State: "+str(state_result))
if state_result == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if state_result == WARN:
    rospy.logwarn("There is a warning in the Server Side")

# Landing the drone
move.linear.x = 0
move.linear.y = 0
move.linear.z = -0.5
move.angular.z = 0
pub.publish(move)
time.sleep(8)

# Stopping movements
move.linear.z = -0.1
pub.publish(move)