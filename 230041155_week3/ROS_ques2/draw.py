#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import threading
import time

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)
        self.mode = 'A' 
        self.square_start_time = None
        
        self.input_thread = threading.Thread(target=self.read_input)
        self.input_thread.daemon = True
        self.input_thread.start()
        
        self.get_logger().info("Use: A=Circle, B=Square, C=Spiral")
        
    def read_input(self):
        while True:
            user_input = input().strip().upper()
            if user_input in ['A', 'B', 'C']:
                self.mode = user_input
                self.square_start_time = None
                self.get_logger().info(f"Mode changed to: {user_input}")
        
    def control_loop(self):
        cmd = Twist()
        
        if self.mode == 'A':  
            cmd.linear.x = 2.0
            cmd.angular.z = 1.0
        elif self.mode == 'B':  
            if self.square_start_time is None:
                self.square_start_time = time.time()
            
            current_time = time.time() - self.square_start_time
            phase = int(current_time) % 4
            
            if phase == 0:  
                cmd.linear.x = 1.0
                cmd.angular.z = 0.0
            elif phase == 1:  
                cmd.linear.x = 0.0
                cmd.angular.z = 1.57  
            elif phase == 2:  
                cmd.linear.x = 1.0
                cmd.angular.z = 0.0
            else:  
                cmd.linear.x = 0.0
                cmd.angular.z = 1.57
        elif self.mode == 'C':  
            cmd.linear.x = 2.0
            cmd.angular.z = 0.5
            
        self.publisher.publish(cmd)

def main():
    rclpy.init()
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()