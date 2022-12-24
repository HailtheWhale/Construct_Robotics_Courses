###############################
# THIS SCRIPT WAS PROVIDED BY THE CONSTRUCT.
###############################

# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions.
rc = RobotControl(robot_name="summit")

# Moving straight forward at 1 m/s for 5 s
forward = rc.move_straight_time("forward",1,5)
print(forward)
# Turn clockwise at 1 m/s for 7 s
turned = rc.turn("clockwise",1,7)
print(turned)