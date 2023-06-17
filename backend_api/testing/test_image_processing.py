import cv2
import unittest
import numpy as np
import mediapipe as mp
from ..modules.image_processing import HandDetectionUtils

mp_hands = mp.solutions.hands


class TestHandDetectionUtils(unittest.TestCase):
    def test_bounding_box_coordinates_calculated_correctly(self):
        hd_utils = HandDetectionUtils(max_hand=2)
        positions = [(0.1, 0.2, 0.3), (0.4, 0.5, 0.6), (0.7, 0.8, 0.9)]
        x_min, y_min, x_max, y_max, width, height = hd_utils.get_bounding_box_coordinates(positions)
        self.assertEqual(x_min, 0)
        self.assertEqual(y_min, 0)
        self.assertEqual(x_max, 0)
        self.assertEqual(y_max, 0)
        self.assertEqual(width, 0)
        self.assertEqual(height, 0)

    def test_get_bounding_box_coordinates_valid_input(self):
        utils = HandDetectionUtils(max_hand=2)
        positions = [(0.1, 0.2, 0.3), (0.4, 0.5, 0.6)]
        result = utils.get_bounding_box_coordinates(positions)
        self.assertIsNotNone(result)

    def test_detect_hands_valid_input(self):
        utils = HandDetectionUtils(max_hand=2)
        image = np.zeros((224, 224, 3), dtype=np.uint8)
        result = utils.detect_hands(image)
        self.assertIsNotNone(result)

    def test_get_image_resized_valid_input(self):
        utils = HandDetectionUtils(max_hand=2)
        copy_image = np.zeros((224, 224, 3), dtype=np.uint8)
        positions = [(0.1, 0.2, 0.3), (0.4, 0.5, 0.6)]
        result = utils.get_image_resized(positions, copy_image)
        self.assertIsNotNone(result)

    def test_init_valid_input(self):
        max_hand = 2
        utils = HandDetectionUtils(max_hand)
        self.assertIsNotNone(utils.hands)

    def test_detect_hands_error(self):
        utils = HandDetectionUtils(max_hand=2)
        image = np.zeros((224, 224, 3), dtype=np.uint8)
        utils.hands.process = unittest.mock.Mock(side_effect=cv2.error())
        result = utils.detect_hands(image)
        self.assertIsNone(result)