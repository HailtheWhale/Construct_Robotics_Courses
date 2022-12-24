# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions. 
rc = RobotControl()

# Applying a class method/ function.  
laser1 = rc.get_laser_full()

# Making dictionary
pos_dict = {"Position 0": laser1[0],"Position 100": laser1[100],"Position 200": laser1[200],"Position 300": laser1[300],"Position 400": laser1[400],"Position 500": laser1[500],"Position 600": laser1[600],"Position 719": laser1[719]}

# Printing dictionary 
print ("The distance dictionary measured is: ", pos_dict)
