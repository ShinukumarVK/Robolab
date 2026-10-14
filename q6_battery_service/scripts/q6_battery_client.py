
#!/usr/bin/env python3

import rospy
from q6_battery_service.srv import BatteryInfo


def battery_client():
    rospy.init_node("battery_info_client")

    rospy.loginfo("Waiting for battery information service...")

    rospy.wait_for_service("get_battery_info")

    try:
        get_battery = rospy.ServiceProxy(
            "get_battery_info",
            BatteryInfo
        )

        response = get_battery()

        print("\n----- BATTERY INFORMATION -----")
        print("Voltage       : {:.2f} V".format(response.voltage))
        print("Temperature   :", response.temperature, "°C")
        print("Charge        : {:.1f} %".format(response.percentage * 100))
        print("Location      :", response.location)
        print("Serial Number :", response.serial_number)
        print("-------------------------------\n")

    except rospy.ServiceException as error:
        rospy.logerr("Service call failed: %s", error)


if __name__ == "__main__":
    battery_client()
