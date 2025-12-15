#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher = self.create_publisher(String, '/keyboard_cmd', 10)

        # snelheid van linker en rechter wiel
        self.left_speed = 0
        self.right_speed = 0

        self.get_logger().info(
            'Keyboard publisher gestart\n'
            'z = sneller\n'
            's = trager\n'
            'a = links draaien\n'
            'x = STOP'
        )

        while rclpy.ok():
            key = input('Commando (z/s/a/x): ').lower()

            if key == 'z':
                self.left_speed += 5
                self.right_speed += 5

            elif key == 's':
                self.left_speed -= 5
                self.right_speed -= 5

            elif key == 'a':
                self.left_speed += 5
                self.right_speed -= 5

            elif key == 'x':
                self.left_speed = 0
                self.right_speed = 0

            else:
                self.get_logger().warn('Ongeldige toets')
                continue

            msg = String()
            msg.data = f'V {self.left_speed} {self.right_speed}'
            self.publisher.publish(msg)

            self.get_logger().info(f'Verstuurd: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardPublisher()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
