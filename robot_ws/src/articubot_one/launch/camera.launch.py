from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            namespace='camera',
            parameters=[{
                'image_size': [640, 480],
                'time_per_frame': [1, 6],
                'camera_frame_id': 'camera_link_optical',
                'video_device': '/dev/video0'   # 👉 Thêm dòng này để sử dụng đúng thiết bị
            }]
        ),

        Node(
            package='articubot_one',
            executable='apriltag_detector_node',
            output='screen',
            parameters=[{
                'image_topic': '/camera/image_raw',
                'camera_info_topic': '/camera/camera_info',
                'output_topic': '/camera/apriltag/image',
                'pose_topic': '/camera/apriltag/poses',
                'tag_family': '36h11',
                'tag_size': 0.08,
                'publish_tf': True,
                'tf_timeout': 1.0
            }]
        )
    ])
