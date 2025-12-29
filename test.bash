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

# --- 検証 ---

# 1. Talkerが "Publish:" という文字を出力しているか確認
# grepコマンドは、見つかれば終了ステータス0、見つからなければ1を返す
cat /tmp/mypkg.log | grep 'Publish:'
[ "$?" = "0" ] || ng "$LINENO"

# 2. Listenerが "Listen:" という文字を出力しているか確認
cat /tmp/mypkg.log | grep 'Listen:'
[ "$?" = "0" ] || ng "$LINENO"

# 3. 計算結果（数字）が含まれているか確認
cat /tmp/mypkg.log | grep 'Double:'
[ "$?" = "0" ] || ng "$LINENO"

# 結果の判定
[ "$res" = 0 ] && echo "OK"
exit $res
