#!/bin/bash

echo 'Moving to my_scripts folder'
cd /home/user/catkin_ws/src/Construct_Robotics_Courses/Introductory_Courses/Linux_Scripts/src
echo 'Listing contents with permissions'
ls -la
echo 'Changing permissions for move_bb8_square.py'

chmod 777 move_bb8_square.py
echo 'Listing contents with permissions AGAIN'
ls -la