#include "rosbot_control/rosbot_class.h"
#include <list>
#include <ros/ros.h>
#include <string>

using namespace std;

list<float> move_and_inform(RosbotClass rosbot, int n_secs) {
  rosbot.move_forward(n_secs);
  float x, y;
  x = rosbot.get_position(1);
  y = rosbot.get_position(2);

  list<float> coordinates({x, y});
  return coordinates;
}

string trajectory(RosbotClass rosbot) {
  rosbot.turn("clockwise", 3);
  rosbot.move_forward(2.0);
  rosbot.turn("counterclockwise", 3);
  rosbot.move_forward(10.0);
  rosbot.turn("clockwise", 2);
  rosbot.move_forward(3.0);

  string message = "Trajectory was successful";
  return message;
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "rosbot_node");

  RosbotClass rosbot;

  ROS_INFO_STREAM("Exercise 3.1");
  int s;
  ROS_INFO_STREAM("How many seconds will the bot move forth?");
  cin >> s; 
  ROS_INFO_STREAM("Moving for " << s << "seconds");

  list<float> coordinates;
  coordinates = move_and_inform(rosbot, s);

  ROS_INFO_STREAM("The final x,y positions recorded are:");
  for (float coor : coordinates){
    cout << coor << ",";
  }

  ROS_INFO_STREAM("Resetting...");
  rosbot.move_backwards(s);

  ROS_INFO_STREAM("Exercise 3.2");
  string m = trajectory(rosbot);
  cout << m << endl;

  return 0;
}

