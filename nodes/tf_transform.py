#!/usr/bin/env python
import rospy
import tf
from std_srvs.srv import Empty, EmptyResponse

restart = False
playing = False

def handle_beginning(req):
    restart = True
    playing = False
    return EmptyResponse()

if __name__ == '__main__':
    rospy.init_node('tf_transform')

    rospy.Service('tf_transform_restart', Empty, handle_beginning)

    listener = tf.TransformListener()

    rate = rospy.Rate(100.0)

    while not rospy.is_shutdown():
        if restart:
            try:
                (trans,rot) = listener.lookupTransform('/world', '/Robot_1/base_link', rospy.Time(0))
                restart = False
                playing = True
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
        elif playing:
            br = tf.TransformBroadcaster()
            br.sendTransform(trans, rot,
                             rospy.Time.now(),
                             "/odom",
                             "/world")
        rate.sleep()
