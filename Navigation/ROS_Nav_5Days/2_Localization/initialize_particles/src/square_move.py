#! /usr/bin/env python
# The requirements forthis exercise are faily extensive, 
# so OOP will be used 
import time
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty, EmptyRequest

class SquareMove():

    def __init__(self):
        # Msg objects 
        self.robot_pose = PoseWithCovarianceStamped()
        self.move = Twist()
        self.srv = EmptyRequest()
        # Pubs, subs 
        self.pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        self.sub = rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped, self.pose_callback)
        # Services 
        rospy.wait_for_service('/global_localization')
        # Create the connection to the service
        self.init_particles_service = rospy.ServiceProxy('/global_localization', Empty)

        # Other stuff 
        self.rate = rospy.Rate(10)
        self.ctrl_c = False
        self.avg_cov = 1
        # If interrupted 
        rospy.on_shutdown(self.shutdown)

    # Shutdown movements 
    def shutdown(self):
        rospy.loginfo("Shutdown!")
        self.stop()
        self.ctrl_c = True

    # Print pose 
    def pose_callback(self,msg):
        self.robot_pose = msg.pose.covariance
        rospy.loginfo("The covariance is:")
        self.robot_pose = msg
        cov_x = self.robot_pose.pose.covariance[0]
        cov_y = self.robot_pose.pose.covariance[7]
        cov_z = self.robot_pose.pose.covariance[35]
        self.avg_cov = (cov_x+cov_y+cov_z)/3
        print(self.avg_cov)
        

    # Move
    def move_forward(self,vel=1.0,duration=30):
        rospy.loginfo("Moving Forward...")
        self.move.linear.x = vel
        i = 0
        while self.ctrl_c == False and i <= duration:
            self.pub.publish(self.move)
            self.rate.sleep()
            i+=1

    # Turn
    def turn(self, z_vel=1.0, duration=14):
        rospy.loginfo("Turning...")
        self.move.linear.x = 0.0
        self.move.linear.y = 0.0
        self.move.angular.z = z_vel
        i = 0
        while self.ctrl_c == False and i <= duration:
            self.pub.publish(self.move)
            self.rate.sleep()
            i+=1

    # Stop moving 
    def stop(self):
        self.move.linear.x = 0.0
        self.move.linear.y = 0.0
        self.move.angular.z = 0.0
        self.pub.publish(self.move)

    # Move in square pattern
    def square_movement(self):
        rospy.loginfo("Performing square movement...")
        for i in range(1,5):
            self.move_forward()
            self.stop()
            self.turn()
            self.stop()
        self.stop()

    # Disperse Particles 
    def disperse(self):
        rospy.loginfo("Dispersing Particles...")
        self.init_particles_service()

if __name__ == '__main__':
    rospy.init_node("square_localizer")

    square_move = SquareMove()
    cov = 1

    while cov >= 0.65:
        square_move.disperse()
        square_move.square_movement()
        cov = square_move.avg_cov
        if cov >= 0.65:
            rospy.loginfo("Covariance average too high. Repeating Process...")
    
    rospy.loginfo("Covariance <= 0.65.")