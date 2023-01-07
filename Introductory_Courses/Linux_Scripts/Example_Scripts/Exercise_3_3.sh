#!/bin/bash

echo 'Moving to my_scripts folder'
cd /home/user/catkin_ws/src/linux_course_files/move_bb8_pkg/Linux_Scripts/Linux_Essentials
echo 'Listing contents with permissions'
ls -la
echo 'Changing permissions or move_bb8_square.py'
chmod 777 move_bb8_square.py
echo 'Listing contents with permissions AGAIN'
ls -la
