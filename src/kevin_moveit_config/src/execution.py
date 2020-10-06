#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "kevin_arm"
group = moveit_commander.MoveGroupCommander(group_name)

joint_goal = group.get_current_joint_values()
joint_goal[0] = 0.0
joint_goal[1] = 0.0
joint_goal[2] = 0.0
joint_goal[3] = 0.0
joint_goal[4] = 0.0

      

# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group.stop()

pose_goal = geometry_msgs.msg.Pose()
"""pose_goal.orientation.w = 0.218578662897
pose_goal.orientation.x = 0.181799433408
pose_goal.orientation.y = -0.244673820136
pose_goal.orientation.z = 0.926988163829"""
"""pose_goal.orientation.w = 0.0
pose_goal.orientation.x = 0.0
pose_goal.orientation.y = 0.0
pose_goal.orientation.z = 0.0
pose_goal.position.x = 0.106290280127
pose_goal.position.y = 0.19710369639
pose_goal.position.z = 0.437325530795
group.set_pose_target(pose_goal)"""
