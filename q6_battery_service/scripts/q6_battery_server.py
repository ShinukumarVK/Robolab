
#!/usr/bin/env python3

import rospy
from q6_battery_service.srv import BatteryInfo, BatteryInfoResponse


def handle_battery_info(request):
    rospy.loginfo("Battery information requested")

    return BatteryInfoResponse(
        voltage=12.4,
        temperature=30.0,
        percentage=0.85,
        location="main battery",
        serial_number="BAT001"
    )


def battery_server():
    rospy.init_node("battery_info_service")

    service = rospy.Service(
        "get_battery_info",
        BatteryInfo,
        handle_battery_info
    )

    rospy.loginfo("Battery information service is ready")
    rospy.spin()


if __name__ == "__main__":
    battery_server()
