#!/usr/bin/python3
import cv2
from utils import Utils, Model_loader
from urllib.request import urlopen
from PIL import Image
import base64
from io import BytesIO
import numpy as np

def process(image, imgSize, num_hands, hand_type):
    Base = Utils(imgSize)
    image = np.array(image)
    image = cv2.flip(image, 1)
    Hands = Base.Hands_model_configuration(False, num_hands, 1)
    with Hands:
        image, result = Base.Hands_detection(image, Hands)
        
        if result.multi_hand_landmarks:
            print(1)
            print(2)
            
            positions = []
            positions =  Base.Detect_hand_type(hand_type, result, positions, image)
            if len(positions) != 0:
                resized_hand = Base.Get_image_resized(positions, image)
                return(resized_hand)
            
        return("sapo")

def url_to_image(canvas_url):
    encoded_data = canvas_url.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    image_stream = BytesIO(decoded_data)
    image = Image.open(image_stream)
    return image
