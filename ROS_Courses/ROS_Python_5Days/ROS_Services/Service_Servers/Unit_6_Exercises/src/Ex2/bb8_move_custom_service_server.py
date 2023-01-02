#! /usr/bin/env python

# So that it waits for the input amount of time 
import time 
import rospy
# Custom msg 
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
# For movement 
from geometry_msgs.msg import Twist

def callback(request):
    # Circular movements 
    move = Twist()
    move.linear.x = 0.3
    move.angular.z = 0.8
    print("Moving in a Circle.")
    pub.publish(move)
    # Continue for given input seconds
    time.sleep(request.duration)
    # Stop
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    # return result. Must be Boolean bc of return type
    return True

# Make node and publisher and service server
rospy.init_node('bb8_service_server') 
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
bb8_circle_service_custom = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage, callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.