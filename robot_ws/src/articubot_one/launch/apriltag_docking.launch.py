from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='articubot_one',
            executable='apriltag_docking_controller',
            output='screen',
            parameters=[{
                'pose_topic': '/camera/apriltag/poses',
                'cmd_vel_topic': '/cmd_vel_tracker',
                'enable_topic': '/dock/enable',
                'status_topic': '/dock/status',
                'target_distance': 0.20,
                'distance_tolerance': 0.02,
                'lateral_tolerance': 0.015,
                'pose_timeout': 0.5,
                'linear_gain': 0.8,
                'angular_gain': 3.0,
                'max_linear_speed': 0.10,
                'min_linear_speed': 0.05,
                'max_angular_speed': 0.55,
                'min_angular_speed': 0.25,
                'search_angular_speed': 0.30,
            }]
        )
    ])
