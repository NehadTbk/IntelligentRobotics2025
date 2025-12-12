from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_pkg',
            executable='battery_publisher',
            output='screen'),
        Node(
            package='my_robot_pkg',
            executable='battery_subscriber',
            output='screen'),
    ])