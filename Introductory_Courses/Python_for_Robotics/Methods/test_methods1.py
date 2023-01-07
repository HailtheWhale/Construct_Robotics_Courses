# For robot napping. 
import time
# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl

# Making a variable with a class. Needed to apply class functions.
rc = RobotControl(robot_name="summit")

time_sleep = int(input("How long is the robot asleep at the wheel? "))
print("Moving forward for " + str(time_sleep) + " Seconds.")

# Exercise wants method
def asleep_at_wheel(nap_time):
    # Moving Forward 
    rc.move_straight()
    # For time_sleep seconds 
    time.sleep(nap_time)
    # Stopping
    rc.stop_robot()

# Calling method 
asleep_at_wheel(time_sleep)