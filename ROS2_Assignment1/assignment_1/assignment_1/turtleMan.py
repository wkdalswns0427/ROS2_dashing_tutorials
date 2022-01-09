import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String, Float32
from mlcs_interface.msg import Position
from geometry_msgs.msg import Twist, Vector3


class TurtleMan(Node):

    def __init__(self):
        self.rad = 1.0
        self.vel = 0.0
        self.dir = True

        self.linear = None
        self.angular = None

        self.linx = 0.0
        self.angz = 0.0
        self.twist = None
        super().__init__('turtle_manipulator')

        self.turtle_sub = self.create_subscription(Position, 'rvd', self.subscribe_message, 10)
        self.turtle_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        self.timer = self.create_timer(1, self.publish_message)
        self.c = 0
    
    def subscribe_message(self, msg):
        self.rad = msg.rad
        self.vel = msg.vel
        self.dir = msg.dir
    
    def publish_message(self):
        self.twist = Twist()
        self.linear = Vector3()
        self.angular = Vector3()

        # x axis velocity
        self.linx = self.vel

        # direction
        if self.dir == True:
            self.angz = self.vel / (self.rad + 1e-6)
        else:
            self.angz = - (self.vel / (self.rad + 1e-6))

        self.linear.x = self.linx
        self.linear.y = 0.0
        self.linear.z = 0.0
        self.angular.x = 0.0
        self.angular.y = 0.0
        self.angular.z = self.angz
        self.twist.linear = self.linear
        self.twist.angular = self.angular

        self.turtle_pub.publish(self.twist)


def main(args=None):
    rclpy.init(args=args)

    turtleNode = TurtleMan()
    try:
        rclpy.spin(turtleNode)
    except KeyboardInterrupt:
        turtleNode.get_logger().info('Keyboard Interrypt (SIGINT)')
    finally:
        turtleNode.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()