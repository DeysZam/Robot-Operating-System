#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


rospy.init_node('decreasing')

pub=rospy.Publisher('dec', Int32, queue_size=1)

rate=rospy.Rate(1)

dcount=0

while not rospy.is_shutdown():

      pub.publish( dcount )

      dcount -= 1
      
      rate.sleep()