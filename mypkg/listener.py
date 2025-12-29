#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        # 'count_up' というトピックを購読
        self.subscription = self.create_subscription(
            Int16,
            'count_up',
            self.cb,
            10
        )

    def cb(self, msg):
        # 受け取った数字を2倍にする計算
        result = msg.data * 2
        # 結果をログに出力
        self.get_logger().info(f'Listen: {msg.data} -> Double: {result}')

def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
