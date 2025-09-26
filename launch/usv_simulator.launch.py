from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():
    # Directories
    stonefish_sim_dir = get_package_share_directory("usv_simulator")
    stonefish_ros2_dir = get_package_share_directory("stonefish_ros2")

    # Arguments
    simulation_data_arg = DeclareLaunchArgument(
        "simulation_data",
        default_value=PathJoinSubstitution([stonefish_sim_dir, "data/drones"]),
        description="Path to the simulation data folder",
    )

    scenario_desc_arg = DeclareLaunchArgument(
        "scenario_desc",
        description="Full path to the scenario file (.scn)",
        default_value=PathJoinSubstitution([stonefish_sim_dir, "data/main.scn"])
    )
    window_res_x_arg = DeclareLaunchArgument(
        "window_res_x", default_value="1920", description="Window width"
    )

    window_res_y_arg = DeclareLaunchArgument(
        "window_res_y", default_value="1080", description="Window height"
    )

    quality_arg = DeclareLaunchArgument(
        "rendering_quality", default_value="high"
    )

    # Include Stonefish simulator launch
    include_stonefish_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([stonefish_ros2_dir, "launch/stonefish_simulator.launch.py"])
        ),
        launch_arguments={
            "simulation_data": LaunchConfiguration("simulation_data"),
            "scenario_desc": LaunchConfiguration("scenario_desc"),
            "window_res_x": LaunchConfiguration("window_res_x"),
            "window_res_y": LaunchConfiguration("window_res_y"),
            "rendering_quality": LaunchConfiguration("rendering_quality"),
        }.items(),
    )

    return LaunchDescription([
        simulation_data_arg,
        scenario_desc_arg,
        window_res_x_arg,
        window_res_y_arg,
        quality_arg,
        include_stonefish_launch,
    ])
