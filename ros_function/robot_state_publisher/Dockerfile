FROM ros:melodic-robot

RUN apt-get update -qq && apt-get install -y -q \
    software-properties-common \
    build-essential \
    cmake \
    apt-transport-https \
    python-catkin-tools \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install ros-melodic-turtlebot3 -y
RUN apt-get install ros-melodic-turtlebot3-msgs

ENV ROS_IP="172.17.0.3" \
    ROS_MASTER_URI="http://core:11311" 

COPY turtlebot3_burger.urdf.xacro /root/turtlebot3_description/turtlebot3_burger.urdf.xacro

COPY robot_state_publisher_launch.sh /root/copy/robot_state_publisher_launch.sh

RUN chmod 774 /root/copy/robot_state_publisher_launch.sh

ENTRYPOINT ["./root/copy/robot_state_publisher_launch.sh"]


