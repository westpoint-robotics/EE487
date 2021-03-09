#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

def servo_sweep():

    rospy.init_node('servo_node', anonymous=True)
    pub = rospy.Publisher('servo', UInt16, queue_size=10)

    #r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # From 0 to 180 degrees
        for angle in range(0,180):
            pub.publish(angle)
            rospy.sleep(0.005)
        # From 180 to 0 degrees
        for angle in range(180,-1,-1):
            pub.publish(angle)
            rospy.sleep(0.005)
        #r.sleep()

if __name__ == '__main__':
    try:
        #Publish servo angle
        servo_sweep()
    except rospy.ROSInterruptException: pass
