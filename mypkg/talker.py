#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'topic', 10)
        self.create_timer(1.0, self.cb)
        self.n = 0

    def cb(self):
        # 計算式を作成 (例: "0 + 5", "1 + 5"...)
        expression = f"{self.n} + 5"
        msg = String()
        msg.data = expression
        self.pub.publish(msg)
        self.get_logger().info(f'Publish: "{expression}"')
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
