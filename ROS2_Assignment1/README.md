# ROS2 Assignment1
## Task
원운동의 회전반경(radius), linear velocity(velocity), 회전방향(direction) 값을 포함하는 ROS 메세지 타입을 정의하고 이 토픽 메세지를 받아 Turtlesim에 속도명령(cmd_vel)을 주는 프로그램을 설계한다. ros2 launch로 turtlesim과 설계한 프로그램을 동시에 실행할 수 있는 launch 파일을 제작한다. turtlesim 실행 후, ros2 topic pub으로 새롭게 정의한 메시지 타입을 publish하여 등속 원운동을 명령한다. C++ / Python등의 언어는 자유롭게 선택하여 진행한다.

## Build
```
cd ~/your_workspace
colcon build --packages-select assignment_1
colcon build --packages-select mlcs_interface
```
open new terminal to refresh source directory

## Launch
```
ros2 launch assignment_1 assignmentLaunch.launch.py
```

## Publish Custom Topic
in new terminal
```
ros2 topic pub --once /rvd mlcs_interface/msg/Position "{rad: 2.0, vel: 2.0, dir: True}"
```
dir True : ccw

dir False : cw
