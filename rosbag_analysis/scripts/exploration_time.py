#!/usr/bin/env python3
import rosbag
import os

# Path ke rosbag
bag_path = os.path.join(os.path.dirname(__file__), '..', 'bagfiles', 'my_flight.bag')

# Buka rosbag
bag = rosbag.Bag(bag_path)
times = []

# Ambil waktu dari topik pose UAV
for topic, msg, t in bag.read_messages(topics=['/CERLAB/quadcopter/pose']):
    times.append(t.to_sec())

# Hitung exploration time
if times:
    exploration_time = max(times) - min(times)
    print(f"Exploration Time: {exploration_time:.2f} seconds")
else:
    print("Tidak ada data di topik /CERLAB/quadcopter/pose")

bag.close()
