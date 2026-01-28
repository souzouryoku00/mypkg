#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'formula_cmd', 10)
        self.n = 0
        
        self.declare_parameter('symbol', '+') # 演算子（デフォルトは足し算）
        self.declare_parameter('num', 5)      # 数字（デフォルトは5）

        self.create_timer(1.0, self.cb)

    def cb(self):
        sym = self.get_parameter('symbol').value
        val = self.get_parameter('num').value

        expression = f"{self.n} {sym} {val}"
        
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
