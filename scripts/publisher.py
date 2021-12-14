#!/usr/bin/python2
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


def pub_sub(left_speed,right_speed):
	pub_right = rospy.Publisher('right_speed', Float64, queue_size=10)
	pub_left = rospy.Publisher('left_speed', Float64, queue_size=10)
	send = "The robot status: %s" % left_speed
	rospy.loginfo(send)
	pub_right.publish(right_speed)
	pub_left.publish(left_speed)

def move():
    # Starts a new node
    rospy.init_node('Motion')

    pub_movfr = rospy.Publisher('/car_control/joint_right_controller/command', Float64, queue_size=10)
    pub_movfl = rospy.Publisher('/car_control/joint_left_controller/command', Float64, queue_size=10)
    pub_movbr = rospy.Publisher('/car_control/joint_back_left_controller/command', Float64, queue_size=10)
    pub_movbl = rospy.Publisher('/car_control/joint_back_right_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    stop=0.0
    status = 0
    target_speed = 0.0
    left_speed = 0.0
    right_speed = 0.0
    left_dir = 1
    right_dir = 1
    control_speed = 0.0
    run = True
    mode = ""

    #Receiveing the user's input
    print("Let's move the robot")
    speed = 5
    distance = 100
    left_speed =left_dir*speed
    right_speed =right_dir*speed

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
     t0 = rospy.Time.now().to_sec()
     current_distance = 0

     while not rospy.is_shutdown():
        #Loop to move the turtle in an specified distance
        while(True):
            #Publish the velocity
            pub_movfl.publish(left_speed)
            pub_movfr.publish(right_speed)
            pub_movbl.publish(left_speed)
            pub_movbr.publish(right_speed)

	    pub_sub(left_speed,right_speed)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
	#After the loop, stops the robot
	#Force the robot to stop
	pub_movfl.publish(stop) # publish the turn command.
	pub_movfr.publish(stop) # publish the turn command.
	pub_movbl.publish(stop) # publish the turn command.
	pub_movbr.publish(stop) # publish the turn command.

	pub_sub(stop,stop)
	run = False

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
