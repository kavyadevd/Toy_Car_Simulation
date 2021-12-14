#!/usr/bin/python2
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your Toy!
---------------------------
Moving around:
       i    
   j   k    l
       ,    
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly
CTRL-C to quit
"""

# Assign each key to motion contributed by both wheels
moveBindings = {
        'i':(1,1),
        'j':(-5,5),
        'l':(5,-5),
        ',':(-1,-1)
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 8

def vels(speed):
    return "currently:\tspeed %s" % (speed)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

    pub_movfr = rospy.Publisher('/car_control/joint_right_controller/command', Float64, queue_size=10)
    pub_movfl = rospy.Publisher('/car_control/joint_left_controller/command', Float64, queue_size=10)
    pub_movbr = rospy.Publisher('/car_control/joint_back_left_controller/command', Float64, queue_size=10)
    pub_movbl = rospy.Publisher('/car_control/joint_back_right_controller/command', Float64, queue_size=10)

    stop=False
    status = 0
    target_speed = 0.0
    left_speed = 0.0
    right_speed = 0.0
    left_dir = 0
    right_dir = 0
    control_speed = 0.0

    try:
        print msg
        print vels(speed)
        while(1):
            key = getKey()
	    # Gives direction using keys i,j,l and ,
            if key in moveBindings.keys():
                left_dir = moveBindings[key][0]
                right_dir = moveBindings[key][1]
		print "left_dir: ",left_dir," right_dir: ",right_dir
            # Gives speed control using keys
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                print vels(speed)
                if (status == 14):
                    print msg
                status = (status + 1) % 15
            elif key == ' ' or key == 'k' :
                stop=True
            elif key == '\x03':
                break

            target_speed = speed 

            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 0.5 )
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 0.5 )
            else:
                control_speed = target_speed

            if stop:
                control_speed = 0
                stop = False
                left_dir = 0
                right_dir = 0

       
            left_speed =left_dir*control_speed
            right_speed =right_dir*control_speed
	    print "left_speed: ",left_speed," right_speed: ",right_speed

            pub_movfl.publish(left_speed) # publish the turn command.
            pub_movfr.publish(right_speed) # publish the turn command.
            pub_movbl.publish(left_speed) # publish the turn command.
            pub_movbr.publish(right_speed) # publish the turn command.


    except Exception as e:
        print e

    finally:
        pub_movfl.publish(left_speed) # publish the turn command.
        pub_movfr.publish(right_speed)
        pub_movbl.publish(left_speed)
        pub_movbr.publish(right_speed)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
