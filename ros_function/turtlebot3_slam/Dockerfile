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
RUN apt-get install ros-melodic-turtlebot3-msgs -y
RUN apt-get install ros-melodic-slam-gmapping -y

ENV ROS_IP="172.17.0.4" \
    ROS_MASTER_URI="http://core:11311" \
    TURTLEBOT3_MODEL="burger"

COPY slam_launch.sh /root/copy/slam_launch.sh

RUN chmod 774 /root/copy/slam_launch.sh

ENTRYPOINT ["./root/copy/slam_launch.sh"]
