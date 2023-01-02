#!/usr/bin/env python
###############################
# THIS SCRIPT WAS PROVIDED BY THE CONSTRUCT.
###############################   

# MODIFIED for the Exercise
# CHANGED parts indicated //////////////////////////

import rospy
import tf
import math

if __name__ == '__main__':
    rospy.init_node('my_moving_carrot_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(5.0)
    turning_speed_rate = 0.1
    while not rospy.is_shutdown():
        t = (rospy.Time.now().to_sec() * math.pi)*turning_speed_rate
        # Map to only one turn maximum [0,2*pi)
        rad_var = t % (2*math.pi)
        # //////////////////////////////////////////
        quaternion = tf.transformations.quaternion_from_euler(0.0,0.0,rad_var)
        br.sendTransform((1.0, 0.0, 0.0),
                         (quaternion[0],quaternion[1],quaternion[2],quaternion[3]),
                         rospy.Time.now(),
                         "moving_carrot",
                         "coke_can")
        # //////////////////////////////////////////
        rate.sleep()

