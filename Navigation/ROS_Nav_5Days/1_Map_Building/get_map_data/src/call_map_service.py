#! /usr/bin/env python

import rospy 
from nav_msgs.srv import GetMap, GetMapRequest

# Start Node 
rospy.init_node('Static_Map_Service_Client')
# Wait for /static_map service
rospy.wait_for_service("/static_map")
# Make connection to service
static_map_service = rospy.ServiceProxy('/static_map',GetMap)
get_map = GetMapRequest()
# Print incoming data 
result = static_map_service(get_map)
print(result.map.info)