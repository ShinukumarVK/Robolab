#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def welcome_callback(msg):
    rospy.loginfo("Received on welcome: %s", msg.data)

def node1():
    rospy.init_node('shinu', anonymous=False)

    pub = rospy.Publisher('hello_class', String, queue_size=10)
    rospy.Subscriber('welcome', String, welcome_callback)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        message = "Hello RAA 26_28 !"
        rospy.loginfo("Publishing: %s", message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass