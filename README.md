# ROS2 dashing folder

all commands are set to source ros2 dashing

### must build colcon_ws before anything
### each packages must be built with colcon build tools

** commands **
* ros2 node
* ros2 topic (ex. ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}")
* ros2 service
* ros2 param
* ros2 action
