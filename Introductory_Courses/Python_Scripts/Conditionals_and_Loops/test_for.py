# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions.
rc = RobotControl()

# Getting whole array of laser scans 
scans = rc.get_laser_full()

# Getting highest values from list.
big_scan = 0
# Loops over all scans 
for scan in scans:
    # Updates if scan bigger than biggest scan
    # ... of course the biggest scan is inf, but we 
    # wouldn't care about that. 
    if (scan > big_scan) & (scan < 100):
        big_scan = scan
    # For visualization 
    else:
        pass

print("The biggest scan is: ", big_scan)

