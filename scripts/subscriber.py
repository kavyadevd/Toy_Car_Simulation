#!/usr/bin/python2
import rospy
from std_msgs.msg import Float64

def callback_left(data):
	rospy.loginfo("Speed for the left wheels is: %s", data.data)

def callback_right(data):
	rospy.loginfo("Speed for the right wheels is: %s", data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('right_speed', Float64, callback_right)
    rospy.Subscriber('left_speed', Float64, callback_left)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
