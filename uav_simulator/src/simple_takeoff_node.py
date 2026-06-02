#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Empty

def main():
    rospy.init_node("simple_takeoff_node")

    # Publisher ke setpoint_pose
    pub_pose = rospy.Publisher("/CERLAB/quadcopter/setpoint_pose", PoseStamped, queue_size=10)
    # Publisher ke takeoff
    pub_takeoff = rospy.Publisher("/CERLAB/quadcopter/takeoff", Empty, queue_size=1)

    rospy.sleep(1)  # Tunggu ROS siap

    # Takeoff command
    pub_takeoff.publish(Empty())
    rospy.loginfo("Takeoff command published")

    # Publish pose sesuai takeoff_height
    takeoff_height = rospy.get_param("~takeoff_height", 1.0)
    pose = PoseStamped()
    pose.header.frame_id = "world"
    pose.pose.position.z = takeoff_height
    pose.pose.orientation.w = 1.0

    rate = rospy.Rate(10)
    for _ in range(50):  # Publish beberapa kali
        pub_pose.publish(pose)
        rate.sleep()

    rospy.loginfo("Hovering at {:.1f} m".format(takeoff_height))
    rospy.spin()

if __name__ == "__main__":
    main()
