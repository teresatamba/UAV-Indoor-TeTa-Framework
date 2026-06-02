# TeTa UAV Autonomy Framework

Welcome to the **TeTa UAV Autonomy Framework**, a versatile and modular framework for autonomous unmanned aerial vehicles (UAVs). This framework comprises distinct components (simulator, perception, mapping, planning, and control) to achieve autonomous navigation, unknown exploration, and target inspection.

**Author**: Teresa Tamba

**Contact Email**: t113999409@ntut.edu.tw

If you find this work helpful, kindly show your support by giving us a free ⭐️.

## Table of Contents
1. [The Autonomy Modules Introduction](#I-The-Autonomy-Modules-Introduction)
2. [Installation Guide](#II-Installation-Guide)
3. [Run Autonomy DEMO](#III-Run-Autonomy-DEMO)
4. [Simulation & Real Flight](#IV-Simulation--Real-Flight)

## I. The Autonomy Modules Introduction
The functionality of each autonomy module included in this framework:
 - ```autonomous_flight
```: The autonomous flight package integrating all other modules for various tasks.
 - ```global_planner```: The global waypoint planner library for autonomous robots.
 - ```map_manager```: The 3D mapping library for autonomous robots.
 - ```onboard_detector
```: The dynamic obstacle detection and tracking algorithm for autonomous robots.
 - ```remote_control```: The Rviz configuration and launch files for visualization.
 - ```time_optimizer```: The optimal trajectory time allocation library for autonomous robots.
 - ```tracking_controller
```: The trajectory tracking controller for autonomous robots.
 - ```trajectory_planner```: The trajectory planning library for autonomous robots.
 - ```uav_simulator
```: The lightweight Gazebo/ROS-based simulator for unmanned aerial vehicles.

## II. Installation Guide
This framework is designed for ROS Noetic with Ubuntu 20.04.

```bash
# step 1: install dependencies
sudo apt install ros-${ROS_DISTRO}-octomap* && sudo apt install ros-${ROS_DISTRO}-mavros* && sudo apt install ros-${ROS_DISTRO}-vision-msgs

# step 2: clone this repo to your workspace
cd ~/catkin_ws/src
git clone [URL-REPO-ANDA]

# step 3: build the workspace
cd ~/catkin_ws
catkin_make

III. Run Autonomy DEMO
This section outlines the primary functionalities: navigation, exploration, and inspection.

a. Autonomous Navigation
roslaunch uav_simulator start.launch
roslaunch remote_control navigation_rviz.launch
roslaunch autonomous_flight navigation.launch

b. Autonomous Exploration
roslaunch uav_simulator start.launch
roslaunch remote_control exploration_rviz.launch 
roslaunch autonomous_flight dynamic_exploration.launch



