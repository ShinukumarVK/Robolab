#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def publisher():
    rospy.init_node('shinu_pubnode', anonymous=False)

    pub = rospy.Publisher('Greetings', String, queue_size=10)

    rate = rospy.Rate(10)
    message = "Hello, I am shinu"

    while not rospy.is_shutdown():
        rospy.loginfo(message)
        
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
