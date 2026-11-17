# 🏥 Autonomous Hospital Delivery Robot – Real-Robot Stack

ROS 2 software for the physical prototype of an autonomous robot that delivers medicine and medical supplies inside a hospital. The robot maps the ward with a LiDAR, localizes itself, navigates corridors with Nav2, and returns to its charging/loading dock using AprilTag-based docking.

▶ **Demo video:** https://youtu.be/vAuWKDqSym8

> This repository contains the **real-robot stack** (Jetson Nano). Two related parts of the project live elsewhere:
> - **AI assistant** (voice Q&A with RAG, medicine-tray control): [AI-Medical-Assistant-Robot](https://github.com/KHAAA123/AI-Medical-Assistant-Robot)
> - **Simulation and evaluation study** (Gazebo hospital environments, C++ Nav2 planner plugins, context-aware planner selection, large-scale closed-loop experiments): a separate project, to be released together with the paper.

---

## 📌 Features

- LiDAR SLAM (SLAM Toolbox) and map-based localization (AMCL)
- Autonomous navigation with Nav2 (NavFn global planner, DWB local controller)
- Return-to-dock and AprilTag-based precise docking
- Camera input from a CSI camera on the Jetson Nano (GStreamer)
- Vision-based ball tracking
- Joystick teleoperation with priority over autonomous commands (`twist_mux`)
- Gazebo simulation of the robot and RViz2 visualization

## 🛡 Safety settings

Configured for slow, predictable motion in hospital corridors:

| Setting | Value | File |
|---|---|---|
| Max linear speed | 0.15 m/s | `config/nav2_params.yaml` |
| Max angular speed | 0.7 rad/s | `config/nav2_params.yaml` |
| Robot radius / obstacle inflation | 0.22 m / 0.55 m | `config/nav2_params.yaml` |
| Manual override | Joystick has highest priority (100) over tracker (20) and navigation (10) | `config/twist_mux.yaml` |
| Command timeout | Each velocity source is dropped after 0.5 s without messages | `config/twist_mux.yaml` |

## 🛠 Hardware

| Component | Model |
|---|---|
| Main computer | NVIDIA Jetson Nano B01 |
| Microcontroller | Arduino (motor and encoder interface) |
| Motor driver | BTS7960 |
| LiDAR | RPLidar A1 |
| Camera | CSI camera |
| Wheel encoders | Incremental encoders |
| Power | 12 V battery |

## 💻 Software

| Machine | Setup |
|---|---|
| Robot (Jetson Nano) | ROS 2 **Foxy** |
| Development / simulation laptop | Ubuntu 22.04, ROS 2 **Humble** |

Main packages: Nav2, SLAM Toolbox, ros2_control, twist_mux, RViz2, Gazebo. Languages: Python and C++.

## 📂 Repository structure

```text
robot_ws/
└── src/
    ├── articubot_one/        # Main robot package: URDF, launch files, Nav2/SLAM config, docking scripts
    ├── csi_camera_reader/    # CSI camera node for Jetson Nano
    ├── diffdrive_arduino/    # ros2_control hardware interface for the Arduino base
    ├── serial_motor_demo/    # Motor test GUI and driver
    ├── rplidar_ros/          # RPLidar driver
    ├── ball_tracker/         # (submodule) vision-based ball tracker
    ├── serial/               # (submodule) serial library
    ├── vision_opencv/        # (submodule) cv_bridge
    └── web_video_server/     # (submodule) video streaming
docs/
└── tf_frames.pdf             # TF tree of the robot
```

## 🚀 Build and run

```bash
git clone --recursive https://github.com/KHAAA123/Hospital-dilivery-robot.git
cd Hospital-dilivery-robot/robot_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

| Task | Command |
|---|---|
| Start the robot (hardware) | `ros2 launch articubot_one launch_robot.launch.py` |
| LiDAR | `ros2 launch articubot_one rplidar.launch.py` |
| Mapping | `ros2 launch articubot_one online_async_launch.py` |
| Save a map after mapping | `ros2 run nav2_map_server map_saver_cli -f <your_map>` |
| Localization on a saved map | `ros2 launch articubot_one localization_launch.py map:=<path_to>/<your_map>.yaml` |
| Navigation | `ros2 launch articubot_one navigation_launch.py` |
| Return to dock | `ros2 launch articubot_one return_to_dock.launch.py` |
| AprilTag docking | `ros2 launch articubot_one apriltag_docking.launch.py` |
| Simulation (laptop) | `ros2 launch articubot_one launch_sim.launch.py` |

## 🧩 Nodes added in this project

All in `articubot_one/scripts/`:

| Node | Purpose |
|---|---|
| `save_dock_pose` | Saves the current pose as the dock pose (`config/dock_pose.yaml`) |
| `return_to_dock` | Sends a Nav2 goal to the saved dock pose |
| `apriltag_detector_node` | Detects AprilTags in the camera image and publishes their poses |
| `apriltag_docking_controller` | Final-approach controller that aligns the robot with the dock tag |
| `laser_filter_node` | Keeps only the configured angular sector of the LiDAR scan (`/scan` → `/scan_filtered`) |
| `scan_qos_republisher` | Republishes scans with sensor-data QoS |
| `odom_tf_republisher` | Publishes the odometry TF |

## 🙏 Credits

This stack builds on open-source work. Third-party packages keep their original licenses.

| Package | Origin |
|---|---|
| `articubot_one` (base template), `diffdrive_arduino`, `serial_motor_demo`, `ball_tracker`, `serial` | Josh Newans / Articulated Robotics: [articubot_one](https://github.com/joshnewans/articubot_one), [diffdrive_arduino](https://github.com/joshnewans/diffdrive_arduino), [serial_motor_demo](https://github.com/joshnewans/serial_motor_demo), [ball_tracker](https://github.com/joshnewans/ball_tracker), [serial](https://github.com/joshnewans/serial) |
| `rplidar_ros` | [Slamtec](https://github.com/Slamtec/rplidar_ros) (BSD) |
| `vision_opencv` | [ros-perception](https://github.com/ros-perception/vision_opencv) |
| `web_video_server` | [RobotWebTools](https://github.com/RobotWebTools/web_video_server) |

## 👥 Team

Developed by the DC Research Group, University of Economics Ho Chi Minh City (UEH), led by Le Hoang Kha. Supervisors: Dr. Dang Tri Dung, Dr. Do Tri Cuong.
