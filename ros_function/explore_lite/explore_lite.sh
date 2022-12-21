#!/bin/bash

source /opt/ros/melodic/setup.bash

rosrun explore_lite explore costmap:=map _tf_prefix:=$ROS_NAMESPACE


