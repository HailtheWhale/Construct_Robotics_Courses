#include "rosbot_control/rosbot_class.h"
#include <ros/ros.h>

#include <string>

using namespace std;

class WallDodger{
public:
    // Constructor 
    WallDodger(string a){
        dir = a;
    };
    // Parameters 
    string dir;
    // inheritance 
    RosbotClass rosbot;
    // Function
    void dodge_wall();
};

void WallDodger::dodge_wall(){
    // Move 
    rosbot.move_forward(1);

    // Check distance 
    while (rosbot.get_laser(0) > 1.5){
        ROS_INFO_STREAM("Distance to wall: " << rosbot.get_laser(0));
        // Move 
        rosbot.move_forward(1);
    }

    // Turn left or turn right?
    if (dir == "left"){
        rosbot.turn("counterclockwise", 4);
        rosbot.move_forward(5);

    } else if (dir == "right"){
        rosbot.turn("clockwise", 4); 
        rosbot.move_forward(5);

    } else {
        ROS_INFO_STREAM("Error in direction. ");
    }
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "Rosbot_move_node");
  // Calling class 
  WallDodger robo1("left");

  robo1.dodge_wall();
}
