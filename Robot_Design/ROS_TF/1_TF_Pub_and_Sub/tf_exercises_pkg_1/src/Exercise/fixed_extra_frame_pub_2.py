#!/usr/bin/env python 
###############################
# THIS SCRIPT WAS PROVIDED BY THE CONSTRUCT.
############################### 

# MODIFIED for the exercise

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('my_fixed_carrot_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(3.0)
    while not rospy.is_shutdown():
        br.sendTransform((1.0, 0.0, 3.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "fixed_carrot",
                         "turtle2")
        rate.sleep()