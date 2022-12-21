#!/bin/bash

source /opt/ros/melodic/setup.bash

rosparam set /robot_description "$(/opt/ros/melodic/bin/xacro /root/turtlebot3_description/turtlebot3_burger.urdf.xacro)"
rosrun robot_state_publisher robot_state_publisher _publish_frequency:=50.0 _tf_prefix:=$ROS_NAMESPACE

