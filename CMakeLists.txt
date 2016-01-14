cmake_minimum_required(VERSION 2.8.3)
project(resibots_launch)

## Find catkin macros and libraries
find_package(catkin REQUIRED)

##Needed for ros packages
catkin_package(CATKIN_DEPENDS rospy hexa_control openni2_launch rtabmap_ros tf std_srvs)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

# install(DIRECTORY config
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
