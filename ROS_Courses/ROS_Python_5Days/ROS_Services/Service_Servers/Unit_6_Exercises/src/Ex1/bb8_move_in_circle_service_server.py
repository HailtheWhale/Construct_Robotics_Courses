#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse  # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def callback(request):
    # Circular movements 
    move = Twist()
    move.linear.x = 0.3
    move.angular.z = 0.8
    print("Moving in a Circle.")
    pub.publish(move)
    # return nothing
    return EmptyResponse()

# Make node and publisher and service server
rospy.init_node('service_server') 
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
bb8_circle_service = rospy.Service('/move_bb8_in_circle', Empty, callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.