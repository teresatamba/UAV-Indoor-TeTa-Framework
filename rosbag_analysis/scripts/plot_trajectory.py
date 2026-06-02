#!/usr/bin/env python3
import rosbag
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # meskipun warning bisa diabaikan

# Path rosbag
bag_path = 'bag_files/flight_data.bag'

# Topic yang ingin dibaca
pose_topic = '/CERLAB/quadcopter/pose'

# Membaca data dari rosbag
positions = []
with rosbag.Bag(bag_path, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=[pose_topic]):
        x = msg.pose.position.x
        y = msg.pose.position.y
        z = msg.pose.position.z
        positions.append((x, y, z))

positions = np.array(positions)

# Dummy nodes planner (contoh)
# nanti bisa diganti dengan data frontier / edge dari planner
x_nodes = positions[::10,0]
y_nodes = positions[::10,1]
z_nodes = positions[::10,2]

# Plot trajectory + nodes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:,0], positions[:,1], positions[:,2], color='blue', label='UAV trajectory')
ax.scatter(positions[0,0], positions[0,1], positions[0,2], color='green', s=50, label='Start')
ax.scatter(positions[-1,0], positions[-1,1], positions[-1,2], color='red', s=50, label='End')
ax.scatter(x_nodes, y_nodes, z_nodes, color='orange', s=30, label='Planner nodes')

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')
ax.legend()
plt.show()
