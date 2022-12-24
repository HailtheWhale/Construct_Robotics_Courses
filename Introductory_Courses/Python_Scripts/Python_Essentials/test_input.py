# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions. 
rc = RobotControl()

# Getting dersired index via user input
index = int(input("What laser scan position (between 0 and 719)? "))

# Applying a class method/ function.  
laser1 = rc.get_laser(index)
# concatenating to give better output.
int_str = "The distance measured at position " + str(index) + " is:"
print (int_str,  laser1)