
#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import BatteryState


def temperature_callback(msg):
    rospy.loginfo(
        "Remote Server - Ambient Temperature: %.2f C",
        msg.data
    )


def battery_callback(msg):
    rospy.loginfo(
        "Remote Server - Battery Information:\n"
        "Voltage: %.2f V\n"
        "Temperature: %.1f C\n"
        "Percentage: %.0f%%\n"
        "Location: %s\n"
        "Serial Number: %s",
        msg.voltage,
        msg.temperature,
        msg.percentage * 100,
        msg.location,
        msg.serial_number
    )


def factory_server_subscriber():
    rospy.init_node('factory_server_subscriber', anonymous=True)

    rospy.Subscriber(
        '/ambient_temperature',
        Float32,
        temperature_callback
    )

    rospy.Subscriber(
        '/battery_info',
        BatteryState,
        battery_callback
    )

    rospy.loginfo("Factory server subscriber started.")
    rospy.spin()


if __name__ == '__main__':
    try:
        factory_server_subscriber()
    except rospy.ROSInterruptException:
        pass
