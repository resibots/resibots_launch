#!/usr/bin/env python
import rospy
import tf
from std_srvs.srv import Empty, EmptyResponse

restart = False
playing = False

def handle_beginning(req):
    global restart
    global playing
    restart = True
    playing = False
    return EmptyResponse()

if __name__ == '__main__':
    global restart
    global playing
    # Init ROS node
    rospy.init_node('odom_transform')

    # Get params with defaults
    rate = rospy.get_param('~rate', 100.0) # 100Hz
    world_frame = rospy.get_param('~world_frame', '/world')
    odom_frame = rospy.get_param('~odom_frame', '/odom')
    base_link_frame = rospy.get_param('~base_link_frame', '/Robot_1/base_link')

    # Publish service
    rospy.Service('odom_transform_restart', Empty, handle_beginning)

    listener = tf.TransformListener()

    rate = rospy.Rate(rate)

    while not rospy.is_shutdown():
        while restart and not rospy.is_shutdown():
            try:
                (trans,rot) = listener.lookupTransform(world_frame, base_link_frame, rospy.Time(0))
                restart = False
                playing = True
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
        if playing:
            br = tf.TransformBroadcaster()
            br.sendTransform(trans, rot,
                             rospy.Time.now(),
                             odom_frame,
                             world_frame)
        rate.sleep()
