#include "rosbot_control/rosbot_class.h"
#include <ros/ros.h>

#include <math.h>
#include <string>

using namespace std;

class RosbotEscape {
public:
  RosbotClass rosbot;
  void escape();
  float dist(float x0, float y0, float x1,float y1);
};

void RosbotEscape::escape() {
  rosbot.move_forward(1);
  float scan_front;
  scan_front = rosbot.get_laser(1);
  // Move until near wall.
  while(scan_front >= 2.0){
    rosbot.move_forward(1);
    scan_front = rosbot.get_laser(1);
  }
  // Turn right.
  rosbot.turn("clockwise", 3);
  rosbot.move_forward(2);
  rosbot.turn("counterclockwise", 2);
  // Move until set distance is travelled.
  float x0,y0,x1,y1,dist_travelled;
  x0 = rosbot.get_position(1);
  y0 = rosbot.get_position(2);
  
  dist_travelled = 0.0;
  while (dist_travelled <= 20.0){
    rosbot.move_forward(1);
    x1 = rosbot.get_position(1);
    y1 = rosbot.get_position(2);
    // Sum distance travelled
    dist_travelled = dist_travelled + dist(x0,y0,x1,y1);
  }
  ROS_INFO_STREAM("Made it. Woo.");
  rosbot.turn("clockwise", 14);
}

float RosbotEscape::dist(float x0, float y0, float x1, float y1){
    float distance;
    distance = sqrt(pow((x1-x0),2)+pow((y1-y0),2));
    return distance;
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "Rosbot_escape");
  RosbotEscape rosbot_escape;
  rosbot_escape.escape();
}