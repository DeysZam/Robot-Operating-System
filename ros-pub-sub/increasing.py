#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


rospy.init_node('increasing')

pub=rospy.Publisher('inc', Int32, queue_size=1)

rate=rospy.Rate(1)

icount=0

while not rospy.is_shutdown():

      pub.publish( icount )

      icount += 1
      
      rate.sleep()