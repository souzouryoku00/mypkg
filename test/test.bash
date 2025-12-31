#!/bin/bash
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo "${1}行目のテスト失敗"
      res=1
}

res=0

if [ -f /opt/ros/humble/setup.bash ]; then
    source /opt/ros/humble/setup.bash
elif [ -f /opt/ros/jazzy/setup.bash ]; then
    source /opt/ros/jazzy/setup.bash
fi

colcon build
source install/setup.bash

timeout 10 env PYTHONUNBUFFERED=1 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1

cat /tmp/mypkg.log | grep 'Publish:'
[ "$?" = "0" ] || ng "$LINENO"

cat /tmp/mypkg.log | grep 'Listen:'
[ "$?" = "0" ] || ng "$LINENO"

cat /tmp/mypkg.log | grep 'Answer: 10'
[ "$?" = "0" ] || ng "$LINENO"

echo "後半"

PYTHONUNBUFFERED=1 ros2 run mypkg listener > /tmp/mypkg_zero.log 2>&1 &
LISTENER_PID=$! 

sleep 2 
timeout 5 ros2 run mypkg talker --ros-args -p symbol:="'/'" -p num:=0 > /dev/null 2>&1

kill $LISTENER_PID

cat /tmp/mypkg_zero.log | grep 'division by zero'
[ "$?" = "0" ] || ng "$LINENO"

[ "$res" = 0 ] && echo "OK"
exit $res
