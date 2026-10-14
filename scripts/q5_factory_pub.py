
#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import BatteryState


def factory_bot_publisher():
    rospy.init_node('factory_bot_publisher', anonymous=True)

    temp_pub = rospy.Publisher(
        '/ambient_temperature', Float32, queue_size=10
    )

    battery_pub = rospy.Publisher(
        '/battery_info', BatteryState, queue_size=10
    )

    def publish_temperature(event):
        msg = Float32()
        msg.data = 28.5
        temp_pub.publish(msg)
        rospy.loginfo("Ambient temperature: %.2f C", msg.data)

    def publish_battery(event):
        msg = BatteryState()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "main_battery"
        msg.voltage = 12.4
        msg.temperature = 30.0
        msg.percentage = 0.85
        msg.location = "main battery"
        msg.serial_number = "BAT001"

        battery_pub.publish(msg)

        rospy.loginfo(
            "Battery: %.2f V, %.1f C, %.0f%%, %s, %s",
            msg.voltage,
            msg.temperature,
            msg.percentage * 100,
            msg.location,
            msg.serial_number
        )

    # Temperature: every 1.0 second (1 Hz)
    rospy.Timer(rospy.Duration(1.0), publish_temperature)

    # Battery: every 0.25 second (4 Hz)
    rospy.Timer(rospy.Duration(0.25), publish_battery)

    rospy.loginfo("Factory bot publisher started.")
    rospy.spin()


if __name__ == '__main__':
    try:
        factory_bot_publisher()
    except rospy.ROSInterruptException:
        pass
