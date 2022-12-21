FROM ros:melodic-ros-base
# install ros tutorials packages
RUN apt-get update && apt-get install -y \
    ros-melodic-ros-tutorials \
    ros-melodic-common-tutorials \
    ros-melodic-turtlesim \
    && rm -rf /var/lib/apt/lists/

ENV ROS_IP="172.17.0.2" 

CMD ["roscore"]
