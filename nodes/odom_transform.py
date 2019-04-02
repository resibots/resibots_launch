#!/usr/bin/env python
import rospy
import tf
from std_srvs.srv import Empty, EmptyResponse

class OdomTransform:
    def __init__(self):
        self.restart = False
        self.playing = False

    def handle_beginning(self, req):
        self.restart = True
        self.playing = False
        return EmptyResponse()

    def loop(self):
        # Get params with defaults
        rate = rospy.get_param('~rate', 100.0) # 100Hz

        world_frame = rospy.get_param('~world_frame', '/world')
        odom_frame = rospy.get_param('~odom_frame', '/odom')
        base_link_frame = rospy.get_param('~base_link_frame', '/Robot_1/base_link')
        print('test')
        # Publish service
        rospy.Service('odom_transform_restart', Empty, self.handle_beginning)

        listener = tf.TransformListener()

        rate = rospy.Rate(rate)

        while not rospy.is_shutdown():
            while self.restart and not rospy.is_shutdown():
                try:
                    (trans,rot) = listener.lookupTransform(world_frame, base_link_frame, rospy.Time(0))
                    self.restart = False
                    self.playing = True
                except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                    continue
            if self.playing:
                br = tf.TransformBroadcaster()
                br.sendTransform(trans, rot,
                                 rospy.Time.now(),
                                 odom_frame,
                                 world_frame)
            rate.sleep()

if __name__ == '__main__':
    # Init ROS node
    rospy.init_node('odom_transform')

    odom_transform_node = OdomTransform()

    odom_transform_node.loop()
