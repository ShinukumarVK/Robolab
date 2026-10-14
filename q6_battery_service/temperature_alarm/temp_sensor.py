#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32


def temp_sensor():
    rospy.init_node('temp_sensor')

    pub = rospy.Publisher(
        '/factory_temp',
        Float32,
        queue_size=10
    )

    rate = rospy.Rate(2)

    rospy.loginfo("Temperature sensor started")

    while not rospy.is_shutdown():
        temperature = random.uniform(25.0, 55.0)
        pub.publish(temperature)

        rospy.loginfo("Temperature reading: %.2f C", temperature)

        rate.sleep()


if __name__ == '__main__':
    temp_sensor()
