import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    package_name = 'articubot_one'

    size = LaunchConfiguration('size')
    square = LaunchConfiguration('square')
    camera_name = LaunchConfiguration('camera_name')

    camera_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory(package_name),
                'launch',
                'camera.launch.py')
        ])
    )

    calibrator = TimerAction(
        period=3.0,
        actions=[
            ExecuteProcess(
                cmd=[
                    'ros2', 'run', 'camera_calibration', 'cameracalibrator',
                    '--size', size,
                    '--square', square,
                    '--camera_name', camera_name,
                    'image:=/camera/image_raw',
                    'camera:=/camera',
                ],
                output='screen')
        ])

    return LaunchDescription([
        DeclareLaunchArgument(
            'size',
            default_value='8x6',
            description='Checkerboard inner-corner count, for example 8x6'),
        DeclareLaunchArgument(
            'square',
            default_value='0.025',
            description='Checkerboard square size in meters'),
        DeclareLaunchArgument(
            'camera_name',
            default_value='usb_composite_device',
            description='Camera name used for the saved calibration YAML'),
        camera_launch,
        calibrator,
    ])
