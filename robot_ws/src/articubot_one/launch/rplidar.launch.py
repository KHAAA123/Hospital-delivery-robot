from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            name='rplidar_node',
            output='screen',
            parameters=[{
               'serial_port': '/dev/ttyUSB1',
                'serial_baudrate': 115200,  # tốc độ chuẩn cho RPLIDAR A1
                'frame_id': 'laser_frame',
                'inverted': False,
                'flip_x_axis': True,
	                'angle_compensate': True,    # nên bật cho dữ liệu quét đều hơn
                'channel_type': 'serial'
            }]
        ),
        Node(
            package='articubot_one',
            executable='scan_qos_republisher',
            name='scan_qos_republisher',
            output='screen',
            parameters=[{
                'input_topic': '/scan',
                'output_topic': '/scan_nav'
            }]
        )
    ])
