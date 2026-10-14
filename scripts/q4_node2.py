#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def welcome_callback(msg):
    rospy.loginfo("Received on hello_class: %s", msg.data)

def node2():
    rospy.init_node('SP2026', anonymous=False)

    pub_welcome = rospy.Publisher('welcome', String, queue_size=10)
    pub_college = rospy.Publisher('hello_college', String, queue_size=10)

    rospy.Subscriber('hello_class', String, welcome_callback)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        welcome_msg = "Hello shinu Welcome !"
        college_msg = "Hello CET!"

        rospy.loginfo("Publishing on welcome: %s", welcome_msg)
        pub_welcome.publish(welcome_msg)

        rospy.loginfo("Publishing on hello_college: %s", college_msg)
        pub_college.publish(college_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass