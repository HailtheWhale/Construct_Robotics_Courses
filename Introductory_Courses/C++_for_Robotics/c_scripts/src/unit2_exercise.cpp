#include "rosbot_control/rosbot_class.h"
#include <ros/ros.h>
#include <list>

int main(int argc, char **argv) {
  ros::init(argc, argv, "rosbot_node");

  RosbotClass rosbot;

  ROS_INFO_STREAM("Exercise 2.1");
  int s;
  int x_lim;
  ROS_INFO_STREAM("How long will the bot try to move?" << endl);
  cin >> s;
  ROS_INFO_STREAM("How far should the bot go?" << endl);
  cin >> x_lim;
  ROS_INFO_STREAM("Moving for " << s << "seconds." << endl);
  rosbot.move_forward(s);

  float x = rosbot.get_position(1);
  if (x >= x_lim){
    ROS_INFO_STREAM("Bot moved far enough. Stopping.");
    rosbot.stop_moving();
  } else{
    ROS_INFO_STREAM("Bot didn't move far enough. Resetting.");
    rosbot.move_backwards(s);
  }
  ROS_INFO_STREAM("Bot reset.");

  ROS_INFO_STREAM("Exercise 2.2");
  ROS_INFO_STREAM("Trying again.");
  rosbot.move_forward(s);

  x = rosbot.get_position(1);
  while (x >= x_lim){
    x = rosbot.get_position(1);
    ROS_INFO_STREAM("Bot moved too far. Reverse.");
    rosbot.move_backwards(1);
  }
  ROS_INFO_STREAM("Bot below distance threshold.");

  ROS_INFO_STREAM("Exercise 2.2");
  ROS_INFO_STREAM("Moving for " << s << "seconds." << endl);
  rosbot.move_forward(s);

  list<float> positions;
  positions = rosbot.get_position_full();

  ROS_INFO_STREAM("The positions recorded are:");
  for (float position : positions){
    ROS_INFO_STREAM(position);
  }

  return 0;
}
