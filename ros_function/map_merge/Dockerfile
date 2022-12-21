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
RUN apt install ros-melodic-multirobot-map-merge -y

ENV TURTLEBOT3_MODEL="burger" 
    
COPY map_merge_launch.sh /root/copy/map_merge_launch.sh

COPY catkin_ws /root/catkin_ws

RUN chmod 774 /root/copy/map_merge_launch.sh

CMD ["./root/copy/map_merge_launch.sh"]
