import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 10)
        self.timer = self.create_timer(0.033, self.timer_callback)
        self.br = CvBridge()
        self.cap = cv2.VideoCapture(0)
    
    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            ros_image = self.br.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(ros_image)
            self.get_logger().info('Publishing video frame')

def main(args=None):
    rclpy.init(args=args)
    video_publisher = VideoPublisher()
    rclpy.spin(video_publisher)
    video_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()