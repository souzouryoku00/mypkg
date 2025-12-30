#!/bin/bash
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo "${1}行目のテスト失敗"
      res=1
}

res=0

source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Publish:'
[ "$?" = "0" ] || ng "$LINENO"

cat /tmp/mypkg.log | grep 'Listen:'
[ "$?" = "0" ] || ng "$LINENO"

cat /tmp/mypkg.log | grep 'Answer:'
[ "$?" = "0" ] || ng "$LINENO"

[ "$res" = 0 ] && echo "OK"
exit $res
