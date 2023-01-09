#include "rosbot_control/rosbot_class.h"
#include <ros/ros.h>

#include <iostream>
#include <list>
#include <map>
#include <string>

using namespace std;

int main(int argc, char **argv) {
  ros::init(argc, argv, "rosbot_node");

  RosbotClass rosbot;

  float coor_x0 = rosbot.get_position(1);
  float coor_y0 = rosbot.get_position(2);
  double time0 = rosbot.get_time();

  ROS_INFO_STREAM("Exercise 1.2");
  ROS_INFO_STREAM("Initial X:  " << coor_x0 << " | Initial Y: " << coor_y0);   
  
  rosbot.move();

  float coor_x1 = rosbot.get_position(1);
  float coor_y1 = rosbot.get_position(2);
  double time1 = rosbot.get_time();
  ROS_INFO_STREAM("Final X: " << coor_x1 << " | Final Y: " << coor_y1 << endl);   

  map<double,float> pos_time_dict;
  pos_time_dict[time0] = coor_x0;
  pos_time_dict[time1] = coor_x1;

  ROS_INFO_STREAM("Exercise 1.3");
  for (auto item : pos_time_dict){
    ROS_INFO_STREAM("Time: "<< item.first << " at Position:" << item.second);
  }

float velocity = (coor_x1-coor_x0)/(time1-time0);

ROS_INFO_STREAM(endl);
ROS_INFO_STREAM("Exercise 1.4");
ROS_INFO_STREAM("Is the bot's Velocity < 1m/s? | " << (velocity <= 1.0) << endl);

return 0;}