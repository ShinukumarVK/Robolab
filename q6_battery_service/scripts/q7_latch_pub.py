#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def publisher():
    rospy.init_node('robot_status_publisher')

    pub = rospy.Publisher(
        '/robot_status',
        String,
        queue_size=10,
        latch=True
    )

    rospy.sleep(1)  # Allow the publisher to initialize

    pub.publish("System Ready")
    rospy.loginfo("Published: System Ready")

    rospy.spin()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
