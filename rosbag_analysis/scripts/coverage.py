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
    positions.append((x, y))

bag.close()

# Konversi ke numpy array
positions = np.array(positions)

# Tentukan resolusi grid (misal 0.5 m per cell)
grid_size = 0.5

# Hitung unique grid cells yang dikunjungi
grid_cells = set((int(x/grid_size), int(y/grid_size)) for x, y in positions)
total_cells = len(grid_cells)

print(f"Number of unique cells visited: {total_cells}")
