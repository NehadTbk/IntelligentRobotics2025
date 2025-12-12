#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher = self.create_publisher(Float32, '/battery_voltage', 10)
        self.timer_period = 1.0 # publish every 60 seconds
        self.timer = self.create_timer(self.timer_period, self.publish_battery)
        self.voltage = 12.5  # starting voltage

    def publish_battery(self):
        # simulate slight battery drain
        self.voltage = max(10.0, self.voltage - random.uniform(0.01, 0.05))
        msg = Float32()
        msg.data = self.voltage
        self.publisher.publish(msg)
        self.get_logger().info(f'Published battery voltage: {self.voltage:.2f} V')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
