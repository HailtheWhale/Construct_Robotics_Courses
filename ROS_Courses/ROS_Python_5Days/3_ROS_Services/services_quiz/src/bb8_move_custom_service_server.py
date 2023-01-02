#! /usr/bin/env python

# To time the movements 
import time
import rospy
# Custom msg 
from services_quiz.srv import BB8CustomServiceMessage
# For movement 
from geometry_msgs.msg import Twist

def callback(request):
    # Movement object  
    move = Twist()
    # Copying the request info to stay organized
    size = request.side
    reps = request.repetitions
    # Redefining size into BIG and SMALL squares 
    if size <= 1:
        size = "small"
        print("Moving in a SMALL square...")
    else:
        size = "big"
        print("Moving in a BIG square...")
    # Moving based on the size 
    i = 0
    # Loop until number of reps is complete.
    while (i < reps):
        i+=1
        # Loop through sides of the SMALL square
        # 4 sides. 
        for side in range(0,4):
            # Turning 
            move.linear.x = 0
            move.angular.z = 0.4
            pub.publish(move)
            # Waiting to complete 90 deg turn
            time.sleep(4)
            # Moving
            move.linear.x = 0.4
            move.angular.z = 0
            pub.publish(move)
            # Waiting based on square size
            if (size == "small"):
                time.sleep(3)
            else:
                time.sleep(6)
            # Stopping
            move.linear.x = 0
            move.angular.z = 0
            pub.publish(move)            

    # return result. Must be Boolean bc of return type
    return True

# Make node and publisher and service server
rospy.init_node('bb8_service_server') 
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
bb8_circle_service_custom = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.