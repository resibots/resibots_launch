# resibots_launch

This package contains launch and configurations files concerning experiments of the ResiBots project.

## Authors
Original author : Konstantinos Chatzilygeroudis

## Dependencies
resibots_launch is basically calling other ResiBots related packages in order to condunct experiments. At this time the following dependencies exist:

* [Openni2] - **openni2_launch**
* [RTABMap] - **rtabmap_ros**
* [hexa_control] - **hexa_control**
* [tf] - **tf**
* [ethzasl_xsens_driver] - **Xsens IMU driver**
* [robot_localization] - **State estimation with fusion of sensors**


## LICENSE

[CeCILL]


[openni2]: http://wiki.ros.org/openni2_launch
[rtabmap]: http://wiki.ros.org/rtabmap_ros
[hexa_control]: https://github.com/resibots/hexa_control
[tf]: http://wiki.ros.org/tf
[CeCILL]: http://www.cecill.info/index.en.html
[ethzasl_xsens_driver]: http://wiki.ros.org/ethzasl_xsens_driver
[robot_localization]: http://wiki.ros.org/robot_localization