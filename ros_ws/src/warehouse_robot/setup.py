from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'warehouse_robot'

setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(exclude=['test']),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        (
            'share/' + package_name,
            ['package.xml']
        ),

        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),

        (
            os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.sdf')
        ),

        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')
        ),

        (
            os.path.join('share', package_name, 'models', 'red_box'),
            glob('models/red_box/*')
        ),

        (
            os.path.join('share', package_name, 'models', 'blue_box'),
            glob('models/blue_box/*')
        ),

        (
            os.path.join('share', package_name, 'models', 'green_box'),
            glob('models/green_box/*')
        ),
    ],

    install_requires=['setuptools'],

    zip_safe=True,

    entry_points={
        'console_scripts': [
             'conveyor_controller = warehouse_robot.conveyor_controller:main',
        ],
    },
)