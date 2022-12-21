#!/bin/bash
set -e
set -u
echo "==> Executing master image entrypoint ..."
echo "-> Setting up ROS"
source "/opt/ros/$ROS_DISTRO/setup.bash"
echo "==> Container ready"
exec "$@"