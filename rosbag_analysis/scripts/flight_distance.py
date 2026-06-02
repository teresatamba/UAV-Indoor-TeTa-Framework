#!/usr/bin/env python3
import rosbag
import os
import numpy as np

# Path ke rosbag
bag_path = os.path.join(os.path.dirname(__file__), '..', 'bagfiles', 'my_flight.bag')

# Buka rosbag
bag = rosbag.Bag(bag_path)
positions = []

# Ambil posisi UAV
for topic, msg, t in bag.read_messages(topics=['/CERLAB/quadcopter/pose']):
    x = msg.pose.position.x
    y = msg.pose.position.y
    z = msg.pose.position.z
    positions.append((x, y, z))

bag.close()

# Konversi ke numpy array
positions = np.array(positions)

# Hitung jarak total
if len(positions) > 1:
    diffs = np.diff(positions, axis=0)
    distances = np.linalg.norm(diffs, axis=1)
    total_distance = np.sum(distances)
    print(f"Total Flight Distance: {total_distance:.2f} meters")
else:
    print("Tidak ada data posisi yang cukup untuk menghitung jarak.")
