#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatterySubscriber(Node):
    def __init__(self):
        super().__init__('battery_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            '/battery_voltage',
            self.listener_callback,
            10
        )
        self.subscription  # avoid unused variable warning

    def listener_callback(self, msg):
        voltage = msg.data
        if voltage < 11.5:
            self.get_logger().warn(f'Battery LOW: {voltage:.2f} V')

def main(args=None):
    rclpy.init(args=args)
    node = BatterySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
