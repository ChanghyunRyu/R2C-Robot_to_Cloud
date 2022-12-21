#!/bin/bash

source /opt/ros/melodic/setup.bash

rosrun tf static_transform_publisher 0 0 0 0 0 0 /map /$ROS_NAMESPACE/map 100

