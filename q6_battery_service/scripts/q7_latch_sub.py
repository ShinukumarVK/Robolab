
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Received: %s", msg.data)

def subscriber():
    rospy.init_node('robot_status_subscriber')
    rospy.Subscriber('/robot_status', String, callback)
    rospy.loginfo("Subscriber is listening to /robot_status")
    rospy.spin()

if __name__ == '__main__':
    subscriber()
