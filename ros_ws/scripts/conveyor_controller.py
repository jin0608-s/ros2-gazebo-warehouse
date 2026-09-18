import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose
from ros_gz_interfaces.srv import SetEntityPose


class ConveyorController(Node):

    def __init__(self):
        super().__init__('conveyor_controller')

        self.client = self.create_client(
            SetEntityPose,
            '/world/warehouse/set_pose'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Gazebo set_pose service waiting...'
            )

        self.boxes = {
            'red_box': -0.15,
            'blue_box': 0.0,
            'green_box': 0.15,
        }

        self.timer = self.create_timer(
            0.05,
            self.move_boxes
        )

    def move_boxes(self):

        for name in self.boxes:

            self.boxes[name] += 0.005

            if self.boxes[name] > 0.30:
                self.boxes[name] = -0.30

            pose = Pose()

            pose.position.x = self.boxes[name]
            pose.position.y = 0.15
            pose.position.z = 0.175

            pose.orientation.w = 1.0

            request = SetEntityPose.Request()
            request.name = name
            request.pose = pose

            self.client.call_async(request)


def main(args=None):

    rclpy.init(args=args)

    node = ConveyorController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()