#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("CET received: %s", msg.data)

def node3():
    rospy.init_node('CET', anonymous=False)

    rospy.Subscriber('hello_college', String, callback)

    rospy.loginfo("CET is listening to hello_college")

    rospy.spin()

if __name__ == '__main__':
    node3()