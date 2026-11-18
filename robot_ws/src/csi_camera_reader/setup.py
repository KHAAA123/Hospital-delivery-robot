from setuptools import setup

package_name = 'csi_camera_reader'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Le Hoang Kha',
    maintainer_email='154750478+KHAAA123@users.noreply.github.com',
    description='ROS 2 node that publishes images from a CSI camera on the Jetson Nano via GStreamer.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'csi_camera_reader_node = csi_camera_reader.csi_camera_reader_node:main'
        ],
    },
)
