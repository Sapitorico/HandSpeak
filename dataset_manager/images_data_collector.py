#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cv2
from utils.utils import Utils
import time


"""
Objective:
The Image_Collection function is used to capture images from a camera feed and save them to a specified directory. The function uses the MediaPipe Hands library to detect hand landmarks in the captured images and allows the user to select which hand to capture. The captured images are resized and saved to the specified directory in a format suitable for training a machine learning model.

Inputs:
- id_cam: the ID of the camera to capture images from
- DATA_PATH: the path to the directory where the captured images will be saved
- action: the action being performed in the captured images
- imgSize: the size to resize the captured images to
- size_data: the total number of images to capture
- num_hands: the maximum number of hands to detect in the captured images
- hand_type: the type of hand to capture (left, right, or all)
- capture_time: the time interval between capturing images

Flow:
1. Initialize the Utils class with the specified parameters
2. Configure the MediaPipe Hands model with the specified parameters
3. While the camera feed is open:
   a. Read a frame from the camera feed
   b. Flip the frame horizontally
   c. Detect hand landmarks in the frame using the MediaPipe Hands model
   d. If the specified hand type is detected:
      i. Draw a bounding box around the hand in the frame
      ii. Resize the hand image to the specified size
      iii. If the 's' key is pressed, save the resized hand image to the specified directory
   e. If the 'esc' key is pressed, exit the loop
4. Release the camera feed and destroy all windows


Additional aspects:
- The function uses the MediaPipe Hands library to detect hand landmarks in the captured images
- The captured images are saved to the specified directory in a format suitable for training a machine learning model
- The function allows the user to select which hand to capture and the time interval between capturing images
- The function uses the Utils class to perform various image processing tasks, such as converting the hand landmarks to YOLO format and drawing bounding boxes around the hands in the captured images.
"""

def Image_Collection(id_cam, DATA_PATH, action, imgSize, size_data, num_hands, hand_type, capture_time):
    capture = cv2.VideoCapture(id_cam)
    Base = Utils(DATA_PATH, action, imgSize, size_data)
    Hands = Base.Hands_model_configuration(False, num_hands, 1)
    key = 0
    k = 0
    count = 0
    time_count = 0
    with Hands:
        while capture.isOpened():
            key = cv2.waitKey(1)
            success, image = capture.read()
            if not success:
                continue
            image = cv2.flip(image, 1)
            image, result = Base.Hands_detection(image, Hands)
            copy_image = image.copy()
            if result.multi_hand_landmarks:
                positions = []
                positions =  Base.Detect_hand_type(hand_type, result, positions, copy_image)
                if len(positions) != 0:
                    Base.Draw_Bound_Boxes(positions, image, hand_type)
                    resized_hand = Base.Get_image_resized(positions, copy_image)
                    if key == 115:
                        k = 1
                    if time_count == capture_time:
                        time_count = 0
                        time.sleep(1)
                    if k == 1:
                        Base.Save_resized_hand(resized_hand, count, hand_type)
                        count += 1
                        time_count+=1
            if key == 27:
                break
            cv2.imshow("image capture", image)
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Image Collection Tool')
    parser.add_argument('--id_cam', type=int, default=0, help='ID of the camera to capture images from')
    parser.add_argument('--data_path', type=str, default='images/Training2', help='Path to the directory where captured images will be saved')
    parser.add_argument('--action', type=str, nargs='+', default=['no'], help='Action being performed in the captured images')
    parser.add_argument('--img_size', type=int, default=224, help='Size to resize the captured images')
    parser.add_argument('--size_data', type=int, default=100, help='Total number of images to capture')
    parser.add_argument('--num_hands', type=int, default=2, help='Maximum number of hands to detect in the captured images')
    parser.add_argument('--hand_type', type=str, default='all', choices=['Left', 'Right', 'all'], help='Type of hand to capture')
    parser.add_argument('--capture_time', type=int, default=None, help='Time interval between capturing images')

    args = parser.parse_args()

    Image_Collection(args.id_cam, args.data_path, args.action, args.img_size, args.size_data, args.num_hands, args.hand_type, args.capture_time)
