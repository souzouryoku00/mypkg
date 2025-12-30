#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.pub = self.create_subscription(String, 'topic', self.cb, 10)

    def cb(self, msg):
        expression = msg.data
        try:
            answer = eval(expression)
            self.get_logger().info(f'Listen: "{expression}" -> Answer: {answer}')
        except Exception as e:
            self.get_logger().error(f'Calculation Failed: {e}')

def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
