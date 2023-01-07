###############################
# THIS SCRIPT WAS PROVIDED BY THE CONSTRUCT.
###############################
# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions. 
rc = RobotControl()

# Applying a class method/ function.  
a = rc.get_laser(360)

print ("The distance measured is: ", a)