#!/usr/bin/python3
import cv2
from urllib.request import urlopen
from PIL import Image
import base64
from io import BytesIO
import numpy as np
from image_processing import HandDetectionUtils
from numbers_model import count_fingers


#Base = HandDetectionUtils(1, 224)
#Hands = Base.hands

def processLetter(image, hand_type):
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
    Base = HandDetectionUtils(1, 224)
    Hands = Base.hands
    with Hands:
        result = Base.detect_hands(image)
        copy_image = image.copy()
        if result.multi_hand_landmarks:
            number = count_fingers(result, copy_image)
            return number
        return("Error, not a hand")



def url_to_image(canvas_url):
    encoded_data = canvas_url.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    image_stream = BytesIO(decoded_data)
    image = Image.open(image_stream)
    return image

      
