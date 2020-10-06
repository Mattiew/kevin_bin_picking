#!/usr/bin/env python

import rospy
import cv2
import rospkg
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from time import time
import sys


rospack = rospkg.RosPack()
base_path = rospack.get_path('image_segmentation')
print('video will be saved at: '+base_path+'/video/')
bridge = CvBridge()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(base_path+'/videos/output_%s.avi'%time(),fourcc, 15, (800,800))

def img_callback(ros_image):
    print('[%s]got an image'%rospy.Time.now())
    global bridge
    global out
    
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, 'bgr8')
    except CvBridgeError as e:
        print(e)
    
    (rows, cos, channels) = cv_image.shape
    
    #ta fonction -> foo(cv_image)

    cv2.imshow('Image', cv_image)
    out.write(cv_image)
    cv2.waitKey(1)

if __name__ == "__main__":
    rospy.init_node('image_reader', anonymous='True')
    
    image_sub = rospy.Subscriber('/camera1/image_raw', Image, img_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')
    cv2.destroyAllWindows()
    out.release()



