#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):
   print msg.data

rospy.init_mode('constant')

sub=rospy.Subscriber('inc', Int32, callback)
sub2=rospy.Subscriber('dec', Inte32, callback)

rospy.spin()





import rospy
from lab5.srv import *