#! /usr/bin/env python

import time
import rospy
import actionlib

from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgResult
# Add twist cmds for movement 
from geometry_msgs.msg import Twist

class AltitudeAdjuster(object):
    
  # create messages that are used to publish feedback/result
  _feedback = CustomActionMsgFeedback()
  _result   = CustomActionMsgResult()

  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("/action_custom_msg_as", CustomActionMsgAction , self.goal_callback, False)
    self._as.start()
    # Initialize publisher
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    # Initialize Twist object 
    self.move = Twist()
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    
    cmd = goal.goal

    # helper variables
    r = rospy.Rate(1)

    # If cmd is TAKEOFF, Takeoff
    if (cmd == "TAKEOFF"):
        # Setting twist movements 
        self.move.linear.z = 0.8

        # Let user know of takeoff 
        rospy.loginfo("Taking off.")

        # To ensure that it publishes takeoff
        for i in range(1,3):
            # Move
            self.pub.publish(self.move)
            # Wait until in the air
            time.sleep(1)
            # Update feedback each second
            self._feedback.feedback = cmd
            # Publish feedback
            self._as.publish_feedback(self._feedback)
        
        # Stop moving up
        self.move.linear.z = 0.05
        self.pub.publish(self.move)

    else:
        # Setting twist movements 
        self.move.linear.z = -1

        # Let user know of takeoff 
        rospy.loginfo("Landing.")

        # To ensure that it publishes takeoff
        for i in range(0,3):
            # Move
            self.pub.publish(self.move)
            # Wait until in the air
            time.sleep(1)
            # Update feedback each second
            self._feedback.feedback = cmd
            # Publish feedback
            self._as.publish_feedback(self._feedback)
        
        # Stop moving up
        self.move.linear.z = -0.1
        self.pub.publish(self.move)

    # the sequence is computed at 1 Hz frequency
    r.sleep()

    self._result = self._feedback
    self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('actions_quiz')
  AltitudeAdjuster()
  rospy.spin()