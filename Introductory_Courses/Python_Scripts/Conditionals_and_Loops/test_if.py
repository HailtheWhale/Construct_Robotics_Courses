# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions.
rc = RobotControl()

# Didn't really intro functions in this lesson,
# BUT will put one here for the sake of making the flowchart.
def print_reading(distance):
    print("The distance in front of the robot is", distance)


laser = rc.get_front_laser()
print("The initial distance is: ", laser)

# If statement only does the check once. Don't want the robot
# running into a wall.
# ...or nevermind. Apparently it was supposed to crash this lesson.
while (laser >= 1):
    # Move Forward
    rc.move_straight()
    print("Distance greater than 1 m. Moving forward. Current Distance is: ", laser)
    # Update Scan
    laser = rc.get_front_laser()

# Stop robot. Print stuff.
rc.stop_robot()
print_reading(laser)
print("Robot Stopped.")