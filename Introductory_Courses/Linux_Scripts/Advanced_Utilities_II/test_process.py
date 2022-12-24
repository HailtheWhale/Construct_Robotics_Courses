#!/usr/bin/env python
###############################
# THIS SCRIPT WAS PROVIDED BY THE CONSTRUCT.
###############################

import rospy
from geometry_msgs.msg import Twist

class MoveBB8():

    def __init__(self):
        self.bb8_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(self.cmd)
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.stop_bb8()
        self.ctrl_c = True

    def stop_bb8(self):
        rospy.loginfo("shutdown time! Stop the robot")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()

    def move_bb8(self, linear_speed=0.2):

        self.cmd.linear.x = -linear_speed
        self.cmd.angular.z = 0

        while not self.ctrl_c:
            self.publish_once_in_cmd_vel()
            rospy.loginfo("Moving BB-8 forward!!")
            self.rate.sleep()

        self.stop_bb8()

if __name__ == '__main__':
    rospy.init_node('process_test', anonymous=True)
    movebb8_object = MoveBB8()
    try:
        movebb8_object.move_bb8()
    except rospy.ROSInterruptException:
        pass
