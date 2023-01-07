# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions.
rc = RobotControl(robot_name="summit")

# These should be self explanatory.
# The turning method definitely does some sort of rounding 
# Behind the scenes. This is good enough to get it into the 
# Room. 
turned = rc.turn("counter-clockwise",1,1)
print(turned)
forward = rc.move_straight_time("forward",1,1)
print(forward)
turned = rc.turn("counter-clockwise",1,1)
print(turned)
forward = rc.move_straight_time("forward",0.5,1.1)
print(forward)
turned = rc.turn("counter-clockwise",1,1)
print(turned)
forward = rc.move_straight_time("forward",0.5,0.5)
print(forward)
turned = rc.turn("clockwise",1,0.3)
print(turned)
forward = rc.move_straight_time("forward",0.3,0.4)
print(forward)
turned = rc.turn("counter-clockwise",1,0.1)
print(turned)
forward = rc.move_straight_time("forward",0.3,5)
print(forward)