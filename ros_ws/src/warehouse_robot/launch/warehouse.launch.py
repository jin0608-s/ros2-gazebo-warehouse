import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    package_share = get_package_share_directory(
        'warehouse_robot'
    )

    bringup_share = get_package_share_directory(
        'open_manipulator_bringup'
    )

    world_without_extension = os.path.join(
        package_share,
        'worlds',
        'warehouse'
    )

    model_path = os.path.join(
        package_share,
        'models'
    )

    gazebo_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=os.pathsep.join([
            model_path,
            os.environ.get('GZ_SIM_RESOURCE_PATH', '')
        ])
    )

    manipulator_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                bringup_share,
                'launch',
                'open_manipulator_x_gazebo.launch.py'
            )
        ),
        launch_arguments={
            'world': world_without_extension
        }.items(),
    )

    set_pose_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/world/warehouse/set_pose@ros_gz_interfaces/srv/SetEntityPose@gz.msgs.Pose@gz.msgs.Boolean'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo_resource_path,
        manipulator_gazebo,
        set_pose_bridge
    ])