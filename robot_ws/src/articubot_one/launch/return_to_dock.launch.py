import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    bringup_dir = get_package_share_directory('articubot_one')

    dock_pose_file = LaunchConfiguration('dock_pose_file')

    return LaunchDescription([
        DeclareLaunchArgument(
            'dock_pose_file',
            default_value=os.path.join(bringup_dir, 'config', 'dock_pose.yaml'),
            description='Full path to the YAML file storing the charging dock pose'),

        Node(
            package='articubot_one',
            executable='return_to_dock',
            output='screen',
            parameters=[{'dock_pose_file': dock_pose_file}]),
    ])
