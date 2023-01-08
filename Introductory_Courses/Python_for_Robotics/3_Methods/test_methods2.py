# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions.
rc = RobotControl(robot_name="summit")

# To get laser scans at given indices 
def laser_vision(a,b,c):
    a_read = rc.get_laser_summit(a)
    b_read = rc.get_laser_summit(b)
    c_read = rc.get_laser_summit(c)
    return[a_read,b_read,c_read]

# Getting inputs 
input1 = int(input("What is the 1st scan index you want? "))
input2 = int(input("What is the 2nd scan index you want? "))
input3 = int(input("What is the 3rd scan index you want? "))

# Calling function 
read_vals = laser_vision(input1,input2,input3)
print("The 1st distance is:", read_vals[0])
print("The 2nd distance is:", read_vals[1])
print("The 3rd distance is:", read_vals[2])
