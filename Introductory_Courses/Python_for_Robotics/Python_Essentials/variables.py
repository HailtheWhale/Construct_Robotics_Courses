# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions. 
rc = RobotControl()

# Applying a class method/ function.  
laser1 = rc.get_laser(360)
# Printing
print ("The 1st distance measured is: ", laser1)

# Applying a class method/ function.  
laser2 = rc.get_laser(480)
print ("The 2nd distance measured is: ", laser2)

# Redefining variable.
laser2 = rc.get_laser(240)
print ("The 2nd REDEFINED distance measured is: ", laser2)

