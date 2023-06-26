#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import mediapipe as mp
import numpy as np
from typing import Tuple, Any, List # Type information

mp_hands = mp.solutions.hands

"""
utils class for image processing, functionalities:
The HandDetectionUtils class provides functionalities for detecting hands in an image using the MediaPipe Hands model. It allows for the detection of a specified number of hands in an image and provides methods for tracking the position of the hands and reshaping the image to focus on the detected hands.

Methods:
- __init__(self, max_hand): initializes the class and creates a MediaPipe Hands model with specified parameters
- detect_hands(self, image: np.ndarray) -> Tuple[np.ndarray, Any]: detects hands in the provided image using the MediaPipe Hands model and returns the image and detection results
- detect_hand_type(hand_type: str, results: Any, copy_img: np.ndarray) -> List[Tuple[float, float, float]]: tracks the position of the specified hand type (left or right) in the image using the detection results and returns a list of positions
- get_bounding_box_coordinates(positions: List[Tuple[float, float, float]]) -> Tuple[int, int, int, int, int, int]: calculates the bounding box coordinates for the detected hand positions and returns them as a tuple
- get_image_resized(self, positions: List[Tuple[float, float, float]], copy_image: np.ndarray) -> np.ndarray: reshapes the image to focus on the detected hands using the provided positions and returns the resized image

Fields:
- imgSize: size to which the image is resized
- offset: the offset used when reshaping the image to focus on the hand
- hands: MediaPipe Hands model used for hand detection
"""


class HandDetectionUtils:
    def __init__(self, max_hand, imgSize=224, offset=10):
        """
        Construct a new 'utils'
        imageSize: size to which the image is resized
        offset: the offset used when reshaping the image to focus on the hand
        max_hand: number of hands to detect

        Return: hands model
        """
        self.imgSize = imgSize
        self.offset = offset
        self.hands = mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=max_hand,
            model_complexity=1,
            min_detection_confidence=0.5,
        )


    def detect_hands(self, image: np.ndarray) -> Tuple[np.ndarray, Any]:

        """
        Hands detection
        image: image to process
        model: hands model
        Return: image and results
        """
        if image is None:
            print('Invalid input: image is None')
            return None
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            result = self.hands.process(image)
            return result
        except cv2.error as e:
            print(f'Error during hand detection: {e}')
            return None



    @staticmethod
    def detect_hand_type(hand_type: str, results , copy_img: np.ndarray) -> List[Tuple[float, float, float]]:
        """
        tracking of the position of the hand in the image, depending on the image chosen by the user

        hand_type: Left or Right hand type
        results: detection results
        positions: list of positions
        copie_img: copy image

        return: position of the hand
        """
        positions = []
        for hand_index, hand_info in enumerate(results.multi_handedness):
            hand_types = hand_info.classification[0].label
            if hand_types == hand_type or hand_type == "all":
                for hand_landmarks in results.multi_hand_landmarks:
                    alto, ancho, c = copy_img.shape
                    for lm in hand_landmarks.landmark:
                        positions.append((lm.x * ancho, lm.y * alto, lm.z * ancho))
        return positions


    @staticmethod
    def get_bounding_box_coordinates(positions: List[Tuple[float, float, float]]) -> Tuple[int, int, int, int, int, int]:
        """
        bounding box coordinates calculation

        positions: list of positions
        Return: coordinates of the bounding box
        """
        x_min = int(min(positions, key=lambda x: x[0])[0])
        y_min = int(min(positions, key=lambda x: x[1])[1])
        x_max = int(max(positions, key=lambda x: x[0])[0])
        y_max = int(max(positions, key=lambda x: x[1])[1])
        width = x_max - x_min
        height = y_max - y_min
        return x_min, y_min, x_max, y_max, width, height

    def get_image_resized(self, positions: List[Tuple[float, float, float]], copy_image: np.ndarray) -> np.ndarray:
        """
        image reshaping

        positions: x y z coordinates
        copie_img: copy frame

        return: redeemed image
        """
        alto, ancho, c = copy_image.shape
        x_min, y_min, x_max, y_max, width, height = self.get_bounding_box_coordinates(positions)
        centro_x, centro_y = int((x_min + x_max) / 2), int((y_min + y_max) / 2)
        lado = max(width, height)
        x1 = max(0, centro_x - int(lado / 2) - 50)
        y1 = max(0, centro_y - int(lado / 2) - 50)
        ancho = min(ancho - x1, int(lado) + 100)
        alto = min(alto - y1, int(lado) + 100)
        x2, y2 = x1 + ancho, y1 + alto
        resized_hand = copy_image[y1:y2, x1:x2]
        resized_hand = cv2.resize(resized_hand, (self.imgSize, self.imgSize), interpolation=cv2.INTER_CUBIC)
        resized_hand = cv2.cvtColor(resized_hand, cv2.COLOR_BGR2RGB)
        return resized_hand
