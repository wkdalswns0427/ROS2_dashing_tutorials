#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            node_executable='turtlesim_node',
            node_name='turtlesim_node',
            output='screen',
        ),
        Node(
            package='assignment_1',
            node_executable='turtleMan',
            node_name='turtleMan',
            output='screen',
        ),
    ])