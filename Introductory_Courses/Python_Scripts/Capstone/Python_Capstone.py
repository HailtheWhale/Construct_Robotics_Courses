# Importing Class made by another python file in the same directory
import time
from robot_control_class_copy import RobotControl


class MazeMouse():
    # Constructing object 
    def __init__(self, celebration_time):
        # Need object to control robot.
        self.robot = RobotControl()
        # Need containers for front and side scans.
        self.scan_right = 0
        self.scan_right_30 = 0
        self.scan_right_60 = 0
        ######
        self.scan_front = 0
        ######
        self.scan_left = 0
        self.scan_left_30 = 0
        self.scan_left_60 = 0

        # Need container for omnifirectional scans.
        self.omni_scan = 0
        # Need containers for celabratory spins
        self.direction = "clockwise"
        self.duration = celebration_time
        self.speed = 3

    # Method for detecting laserscans right, middle, left
    def laser_check_dir(self):
        # print("Providing directional scans.")

        # WOULD use get_laser from Construct's object, 
        # BUT, it seems to be broken sometimes. Thinking that
        # indices are out of bounds, when they shouldn't be.  
        self.scan_right = self.omni_scan[0]
        self.scan_right_30 = self.omni_scan[59]
        self.scan_right_60 = self.omni_scan[129]
        self.scan_left = self.omni_scan[719]
        self.scan_left_30 = self.omni_scan[539]
        self.scan_left_60 = self.omni_scan[629]

        # Getting multiple scans and taking the minimum from them.
        scan_front_1 = self.omni_scan[360]
        scan_front_2 = self.omni_scan[320]
        scan_front_3 = self.omni_scan[400]
        scans = [scan_front_1,scan_front_2,scan_front_3]
        self.scan_front = min(scans)

        # print("Right scan distance is: ", self.scan_right)
        # print("Front scan distance is: ", self.scan_front)
        # print("Left scan distance is: ", self.scan_left)

        return [self.scan_right,self.scan_right_30,self.scan_right_60,self.scan_front,self.scan_left,self.scan_left_30,self.scan_left_60]

    def laser_check_omni(self):
        # print("Providing omni_directional scans.")
        # print("Length of the array is:", len(self.robot.get_laser_full()))
        self.omni_scan = self.robot.get_laser_full()
        return self.omni_scan

    # Method for moving forward
    def move_forward_fast(self):
        print("Getting out of that Maze. Blazing fast.")
        self.robot.move_straight()
        time.sleep(1)
        self.robot.stop_robot()

    def move_forward_slow(self):
        print("Getting out of that Maze. Slowly.")
        self.robot.move_straight_time("forward",0.3,1)
    
    # Method for turning
    def turning(self,deg):
        # Turning for 30 deg
        self.robot.rotate(deg)

    # Method for celebratory spins 
    def celebration(self):
        self.robot.turn(self.direction,self.duration,self.speed)

if __name__ == '__main__':
    # Making object
    rc = MazeMouse(4)
    out_maze = False
    check_front = False
    while not out_maze:
        # Get laser scans 
        omni_lasers = rc.laser_check_omni()
        dir_lasers = rc.laser_check_dir()
        # Check Omni_lasers. If all distances large, out of maze. 
        for i in range(len(omni_lasers)):
            # print(omni_lasers[i])
            # If any of the walls are close, not out of the maze. 
            # Front of robot 
            if omni_lasers[i] < 15:
                break
            # If no checks failed, out of the maze. 
            if i == len(omni_lasers)-1:
                print("Out of the Maze!")
                out_maze = True

        # If Robot escaped, no need to continue
        if out_maze is True:
            break
        # Otherwise, do the things.
        # print("directional lasers")
        # print(dir_lasers[0])
        # print(dir_lasers[1])
        # print(dir_lasers[2])

        # Wall is far away...
        if omni_lasers[359] >= 15 and omni_lasers[329] >= 15 and omni_lasers[389] >= 15:
            print("There's the exit!!!!")
            print("Zooooom!!! Zoooooom!!!")
            rc.move_forward_fast()
            rc.move_forward_fast()
            rc.move_forward_fast()
            rc.move_forward_fast()
            rc.move_forward_fast()
        elif dir_lasers[3] < 15 and dir_lasers[3] >= 2:
            print("Zooooom!!!")
            rc.move_forward_fast()

        # Wall is kind of close
        elif dir_lasers[3] > 1 and dir_lasers[3] < 2:
            print("Tippy toes.")
            rc.move_forward_slow()
        # There's a wall!
        else:
            print("Welp, that's a wall.")
            # Check left and right sides 
            if dir_lasers[-1] < 1 or dir_lasers[-2] < 1 or dir_lasers[-3] < 1:
                print("Right side clear! Turning right!")
                # Doing 45 deg to play it safe
                rc.turning(45)
            elif dir_lasers[0] < 1 or dir_lasers[1] < 1 or dir_lasers[2] < 1:
                print("Left side clear! Turning left!")
                # Doing 45 deg to play it safe
                rc.turning(-45)
            else:
                print("Welp, I'm confused now. I'm just going to look around.")
                rc.turning(90)
    
    # Finally out of the Maze. Celebrate!
    print("I'm Freeeeee!!!!")
    rc.celebration()