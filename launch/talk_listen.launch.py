#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    symbol_arg = launch.actions.DeclareLaunchArgument(
        'symbol',
        default_value='+',
        description='Calculation symbol'
    )
    
    num_arg = launch.actions.DeclareLaunchArgument(
        'num',
        default_value='5',
        description='Calculation number'
    )

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        parameters=[{
            'symbol': launch.substitutions.LaunchConfiguration('symbol'),
            'num': launch.substitutions.LaunchConfiguration('num'),
        }]
    )

    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
    )

    return launch.LaunchDescription([
        symbol_arg,
        num_arg,
        talker,
        listener,
    ])
