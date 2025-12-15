#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class CmdVelSubscriber(Node):
    def __init__(self):
        super().__init__('cmdvel_subscriber')

        self.subscription = self.create_subscription(
            String,
            '/keyboard_cmd',
            self.callback,
            10
        )

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('CmdVel subscriber gestart')

    def callback(self, msg):
        parts = msg.data.split()

        if len(parts) != 3 or parts[0] != 'V':
            self.get_logger().warn('Ongeldig commando')
            return

        left_speed = int(parts[1])
        right_speed = int(parts[2])

        twist = Twist()

        # simpele conversie (demo-doeleinden)
        twist.linear.x = (left_speed + right_speed) / 200.0
        twist.angular.z = (right_speed - left_speed) / 100.0

        self.cmd_pub.publish(twist)

        self.get_logger().info(
            f'Cmd_vel -> linear: {twist.linear.x:.2f}, angular: {twist.angular.z:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
