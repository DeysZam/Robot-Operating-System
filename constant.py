#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from Task2.msg import two_ints

msg = two_ints()
result = Int32()

def callback(i):
    msg.a = i.data

def callback2(d):
    msg.b = d.data    
    
def callback3(msg):
    result.data = msg.a + msg.b
    rospy.loginfo(result)


rospy.init_node('constant')

sub = rospy.Subscriber('inc', Int32, callback)
sub2 = rospy.Subscriber('dec', Int32, callback2)
sub3 = rospy.Subscriber('two_ints', two_ints, callback3)

pub = rospy.Publisher('const', Int32, queue_size=1)

rate=rospy.Rate(1)

while not rospy.is_shutdown():

    pub.publish(result)

    rate.sleep()


#sub=rospy.Subscriber('inc', Int32, callback)
#sub2=rospy.Subscriber('dec', Inte32, callback)