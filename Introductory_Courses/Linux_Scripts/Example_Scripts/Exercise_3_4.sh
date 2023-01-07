#!/bin/bash

ARG1=$1
			
cd /home/user/catkin_ws/src/linux_course_files/move_bb8_pkg/src

if [ "$ARG1" == 'circle' ]; then
    echo "Moving in a CIRCLE!";
	python move_bb8_circle.py
elif [ "$ARG1" == 'forward_backward' ]; then
    echo "Moving BACK and FORWARD!";
	python move_bb8_forward_backward.py
elif [ "$ARG1" ==  'square'  ]; then
    echo "Moving in a SQUARE!";
	python move_bb8_square.py

else
echo "Please enter one of the following after calling this script:
circle
forward_backward
square"

fi
