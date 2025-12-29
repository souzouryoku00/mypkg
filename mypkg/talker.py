#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(Int16, 'count_up', 10)
        self.n = 0
        self.timer = self.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publish: {msg.data}')
        self.n += 1

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
