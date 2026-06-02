#!/usr/bin/env python3

import rosbag
import matplotlib.pyplot as plt
import numpy as np

# Path ROS bag
bag_path = "/home/t2/rosbag_exploration_info/exploration_info.bag"

# Topic yang berisi roadmap / posisi UAV
# Ubah sesuai topic ROS-mu
topic_positions = "/tracking_controller/target_pose"

x_list = []
y_list = []

# Membaca ROS bag
with rosbag.Bag(bag_path, "r") as bag:
    for topic, msg, t in bag.read_messages(topics=[topic_positions]):
        # Ambil posisi dari msg.pose.position
        x = msg.position.x
        y = msg.position.y

        x_list.append(x)
        y_list.append(y)

# Convert ke numpy array
x_array = np.array(x_list)
y_array = np.array(y_list)

# Plot roadmap
plt.figure(figsize=(8, 6))
plt.plot(x_array, y_array, "-o", markersize=3, color="blue", label="UAV Roadmap")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.title("UAV Roadmap from ROS Bag")
plt.grid(True)
plt.legend()
plt.axis("equal")  # Agar skala X dan Y sama
plt.show()
