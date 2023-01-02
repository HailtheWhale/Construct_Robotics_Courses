#! /usr/bin/env python

import time
import rospy
import actionlib

from actionlib.msg import TestAction, TestResult, TestFeedback
# Add twist cmds for movement 
from geometry_msgs.msg import Twist

class SquareFlyer(object):
    
  # create messages that are used to publish feedback/result
  _feedback = TestFeedback()
  _result   = TestResult()

  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("square_flyer", TestAction , self.goal_callback, False)
    self._as.start()
    # Initialize publisher
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    # Initialize Twist object 
    self.move = Twist()
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    
    # helper variables
    r = rospy.Rate(1)
    success = True

    # Initializing twist movements 
    self.move.linear.x = 0
    self.move.linear.y = 0
    self.move.linear.z = 1
    self.move.angular.x = 0
    self.move.angular.y = 0
    self.move.angular.z = 0

    # Let user know of takeoff 
    rospy.loginfo("Taking off.")

    # To ensure that it publishes takeoff
    for i in range(0,5):
        # Move
        self.pub.publish(self.move)
        # Wait until in the air
        time.sleep(1)
    
    # Stop moving up
    self.move.linear.z = 0
    self.pub.publish(self.move)
        
    # Square Movement
    size = goal.goal
    # 4 sides
    for i in range(1, 5):
      # check that preempt (cancelation) has not been requested by the action client
      if self._as.is_preempt_requested():
        rospy.loginfo('The goal has been cancelled/preempted')
        # the following line, sets the client in preempted state (goal cancelled)
        self._as.set_preempted()
        success = False
        # Land the drone 
        rospy.loginfo('Landing the Drone...')
        self.move.linear.x = 0
        self.move.linear.y = 0
        self.move.linear.z = -0.5
        self.pub.publish(self.move)
        time.sleep(12)

        # Stopping movements
        self.move.linear.z = -0.1
        self.pub.publish(self.move)
        break

      # Determine x and y movements
      if (i == 1):
        move_x = 0.5
        move_y = 0
      elif (i == 2):
        move_x = 0
        move_y = 0.5
      elif (i == 3):
        move_x = -0.5
        move_y = 0
      else:
        move_x = 0
        move_y = -0.5

      # Do the square 
      rospy.loginfo('Moving in a square...')
      self.move.linear.x = move_x
      self.move.linear.y = move_y
      self.pub.publish(self.move)
      time.sleep(size)

      # update feedback with side of square
      self._feedback.feedback = i
      # publish feedback
      self._as.publish_feedback(self._feedback)
      # the sequence is computed at 1 Hz frequency
      r.sleep()
    
    # Either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then publish the final result
    # If not success, do not publish anything in the result
    if success:
      self._result.result = (size*4)
      rospy.loginfo('Completed Square in %i seconds' % self._result.result)
      self._as.set_succeeded(self._result)

      # Land the drone 
      rospy.loginfo('Landing the Drone...')
      self.move.linear.x = 0
      self.move.linear.y = 0
      self.move.linear.z = -0.5
      self.move.angular.z = 0
      self.pub.publish(self.move)
      time.sleep(8)

      # Stopping movements
      self.move.linear.z = -0.1
      self.pub.publish(self.move)
      
if __name__ == '__main__':
  rospy.init_node('square_flyer')
  SquareFlyer()
  rospy.spin()