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
RUN apt-get install ros-melodic-move-base -y
RUN apt-get install ros-melodic-dwa-local-planner -y
RUN apt-get install git -y

RUN mkdir catkin_ws
RUN mkdir catkin_ws/src
WORKDIR /catkin_ws/src

WORKDIR /

ENV ROS_IP="172.17.0.8" \
    ROS_MASTER_URI="http://core:11311" \
    TURTLEBOT3_MODEL="burger"

COPY move_base.sh /root/copy/move_base.sh
COPY turtlebot3/ /catkin_ws/src/turtlebot3/
COPY turtlebot3_nps/ /catkin_ws/src/turtlebot3_nps/

RUN chmod 774 /root/copy/move_base.sh

CMD ["./root/copy/move_base.sh"]
