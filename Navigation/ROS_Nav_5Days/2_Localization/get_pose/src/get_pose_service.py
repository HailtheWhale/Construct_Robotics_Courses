#! /usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse  # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose

robot_pose = Pose()

def callback(request):
    print("Robot Pose is:")
    print(robot_pose)
    # return nothing
    return EmptyResponse()

def pose_callback(msg):
    global robot_pose
    robot_pose = msg.pose.pose


# Make node and publisher and service server
rospy.init_node('pose_service_server') 
get_pose_service = rospy.Service('/get_pose_service', Empty, callback) 
rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped, pose_callback)
rospy.spin() # maintain the service open.