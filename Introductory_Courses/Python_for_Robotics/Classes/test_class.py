# Importing Class made by another python file in the same directory
from robot_control_class import RobotControl


class SquareDancer():
    # Constructing object 
    def __init__(self):
        # Need object to control robot. That's it. 
        self.robot = RobotControl(robot_name="summit")

    # Getting out of hall 
    def prepping(self):
        print("Getting out of that hallway. Blazing fast.")
        self.robot.move_straight_time("forward",3,1)
        self.robot.turn("clockwise",1,1)
        self.robot.move_straight_time("forward",3,0.5)

    # Doing the squares based on size
    def square(self,size):
            # only difference between square sizes is the speed. 
        if (size == "small"):
            print("Going to do a small square.")
            speed = 0.5
        elif (size == "big"):
            print("Going to do a big square.")
            speed = 1
        else:
            print("That's not 'big' or 'small'!")

        # Squares have 4 identical sides, so can loop. 
        for sides in range(4):
            print("On side of square: ", sides + 1)
            self.robot.turn("counter-clockwise",1,1)
            self.robot.move_straight_time("forward",speed,1)

# Making object 
robot_dancer = SquareDancer()
# Calling the methods
robot_dancer.prepping()
robot_dancer.square("small")
robot_dancer.square("big")
