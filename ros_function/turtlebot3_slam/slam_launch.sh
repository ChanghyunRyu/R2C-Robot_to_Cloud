#!/bin/bash

source /opt/ros/melodic/setup.bash

echo "Slam application launching"
roslaunch turtlebot3_slam turtlebot3_gmapping.launch set_base_frame:=$ROS_NAMESPACE/base_footprint set_odom_frame:=$ROS_NAMESPACE/odom set_map_frame:=$ROS_NAMESPACE/map

