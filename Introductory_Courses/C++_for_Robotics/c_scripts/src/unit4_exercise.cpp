#include "ros/console.h"
#include "rosbot_control/rosbot_class.h"
#include <list>
#include <ros/ros.h>
#include <string>
#include<float.h>

using namespace std;

void wall_reads(RosbotClass rosbot) {
  float left, right;
  left = rosbot.get_laser(700);
  right = rosbot.get_laser(20);

  float coordinates[] = {left, right};
  ROS_INFO_STREAM("The Left Distance:" << coordinates[0] << " | The Right Distance is " << coordinates[1]);
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "rosbot_node");

  RosbotClass rosbot;

  int s;
  ROS_INFO_STREAM("Exercise 4.1");
  ROS_INFO_STREAM("How long will the bot try to move?" << endl);
  cin >> s;
  ROS_INFO_STREAM("Moving for " << s << "seconds");
  rosbot.move_forward(s);

  wall_reads(rosbot);
  ROS_INFO_STREAM("Resetting...");
  rosbot.move_backwards(s);

  ROS_INFO_STREAM("Exercise 4.2");
  ROS_INFO_STREAM("Moving for " << s << "seconds");
  rosbot.move_forward(s);
  
  float* laser_data;
  laser_data = rosbot.get_laser_full();

  ROS_INFO_STREAM("Laser Values: ");
  for (int i = 0; i < 720; i++)
  {
  ROS_INFO_STREAM(*laser_data);
  laser_data++;  
  }
  return 0;
}
