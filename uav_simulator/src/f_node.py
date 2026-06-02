#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped
import time

rospy.init_node('takeoff_loop')
pub = rospy.Publisher('/CERLAB/quadcopter/setpoint_pose', PoseStamped, queue_size=10)

takeoff_height = rospy.get_param('/takeoff_height', 1.0)
rate = rospy.Rate(20)  # 20 Hz

pose = PoseStamped()
pose.header.frame_id = "world"
pose.pose.position.x = 0.0
pose.pose.position.y = 0.0
pose.pose.position.z = takeoff_height
pose.pose.orientation.w = 1.0

start_time = rospy.Time.now()
while (rospy.Time.now() - start_time).to_sec() < 5.0:  # hold 5 detik
    pub.publish(pose)
    rate.sleep()

rospy.loginfo("Takeoff complete at {:.2f} m".format(takeoff_height))
