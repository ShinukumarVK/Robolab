
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(msg):
    rospy.loginfo("Received: %s", msg.data)


def subscriber():
    rospy.init_node('RAA26_subnode', anonymous=False)

    rospy.Subscriber('Greetings', String, callback)

    rospy.loginfo("Subscriber is listening to Greetings")
    rospy.spin()


if __name__ == '__main__':
    subscriber()
