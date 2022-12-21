#!/bin/bash

source /opt/ros/melodic/setup.bash

unset ROS_NAMESPACE

echo "Slam application launching"

cd /catkin_ws
catkin_make
source devel/setup.bash

roslaunch turtlebot3_nps move_base_namespace.launch robot_namespace:=tb3_0

