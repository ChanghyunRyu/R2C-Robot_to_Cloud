#!/bin/bash

source /opt/ros/melodic/setup.bash

cd /root/catkin_ws
rm -rf devel build
catkin_make
source devel/setup.bash

roslaunch a multi_map_merge.launch 



