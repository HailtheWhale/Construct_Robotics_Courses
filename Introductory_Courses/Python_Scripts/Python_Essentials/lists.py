# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions. 
rc = RobotControl()

# Applying a class method/ function.  
laser1 = rc.get_laser_full()
# Printing via indexing 
print ("The right distance measured is: ", laser1[0])
print ("The front distance measured is: ", laser1[360])
print ("The left REDEFINED distance measured is: ", laser1[719])