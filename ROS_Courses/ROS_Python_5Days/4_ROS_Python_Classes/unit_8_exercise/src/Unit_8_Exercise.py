#! /usr/bin/env python

import rospy
# Custom msg 
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage
# Import the class 
from bb8_move_circle_class import MoveBB8

def callback(request):
    # instantiate class 
    bb8 = MoveBB8()
    # Move and stop. Taken care of by modified class.
    bb8.move_bb8(dur=request.duration)
    # return result. Must be Boolean bc of return type
    return True

# Make node and service server
rospy.init_node('bb8_service_server') 
bb8_circle_service_custom = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage, callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.