#!/usr/bin/python3
import cv2
import numpy as np
from image_processing import HandDetectionUtils
from control_hand import HandControl


def processLetter(image, hand_type):
    """
    Function that recieves the stream frame (image) and the hand_type.
    Returns: if success: an isoleted and resized image of the hand
                   else: string "Error, not a hand" 
    """
    Base = HandDetectionUtils(1, 224)
    Hands = Base.hands
    image = cv2.flip(image, 1)
    with Hands:
        result = Base.detect_hands(image)
        copy_image = image.copy()
        if result.multi_hand_landmarks:
            positions = Base.detect_hand_type(hand_type, result, copy_image)
            if len(positions) != 0:
                resized_hand = Base.get_image_resized(positions, copy_image)
                return resized_hand
            
        return("Error, not a hand")
    
def processNumber(image):
    """
    Function that recieves the stream frame (image)
    Returns: if success: The number taht has been obtained with count_fingers fucntion
                   else: string "Error, not a hand"
    """
    Base = HandDetectionUtils(224)
    control = HandControl()
    Hands = Base.hands
    image = cv2.flip(image, 1)
    with Hands:
        result = Base.detect_hands(image)
        copy_image = image.copy()
        if result.multi_hand_landmarks:
            number = control.count_fingers(copy_image, result)
            return number
        return("Error, not a hand")