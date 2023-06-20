#!/usr/bin/env python
# -*- coding: utf-8 -*-
from image_processing import mp_drawing

"""
Objective:
The objective of the 'count_fingers' function is to count the number of fingers that are visible in an image of a hand using the results obtained from the MediaPipe Hand Detection model.

Inputs:
- 'results': the results obtained from the MediaPipe Hand Detection model, which includes the landmarks of the hand.
- 'image': the image of the hand.

Flow:
- Initialize 'fingerCount' to 0.
- Get the height and width of the image.
- If there are multiple hand landmarks detected:
  - For each hand landmark:
    - Get the hand type (left or right).
    - Get the landmarks for the thumb tip and pinky tip.
    - If the thumb tip is to the left of the pinky tip and the hand type is right:
      - Get the y-coordinate of the thumb tip.
      - Get the y-coordinates of the index, middle, ring, and pinky pip landmarks.
      - Get the x-coordinate of the index MCP landmark.
      - Get the y-coordinates of the index, middle, ring, and pinky tip landmarks.
      - Calculate the difference between the x-coordinate of the thumb IP landmark and the x-coordinate of the index MCP landmark.
      - If the finger positions indicate one finger is extended, set 'fingerCount' to 1.
      - If the finger positions indicate two fingers are extended, set 'fingerCount' to 2.
      - If the finger positions indicate three fingers are extended, set 'fingerCount' to 3.
      - If the finger positions indicate four fingers are extended, set 'fingerCount' to 4.
      - If the finger positions indicate five fingers are extended, set 'fingerCount' to 5.
    - If the thumb tip is to the right of the pinky tip and the hand type is left:
      - Get the y-coordinate of the thumb tip.
      - Get the y-coordinates of the index, middle, ring, and pinky pip landmarks.
      - Get the x-coordinate of the index MCP landmark.
      - Get the y-coordinates of the index, middle, ring, and pinky tip landmarks.
      - Calculate the difference between the x-coordinate of the thumb IP landmark and the x-coordinate of the index MCP landmark.
      - If the finger positions indicate one finger is extended, set 'fingerCount' to 1.
      - If the finger positions indicate two fingers are extended, set 'fingerCount' to 2.
      - If the finger positions indicate three fingers are extended, set 'fingerCount' to 3.
      - If the finger positions indicate four fingers are extended, set 'fingerCount' to 4.
      - If the finger positions indicate five fingers are extended, set 'fingerCount' to 5.
- Return 'fingerCount'.

Outputs:
- 'fingerCount': the number of fingers that are visible in the image of the hand.

Additional aspects:
- The function uses the MediaPipe Hand Detection model to obtain the landmarks of the hand.
- The function uses the 'mp_drawing' module from the 'image_processing' package to convert the normalized landmark coordinates to pixel coordinates.
- The function assumes that the hand in the image is either a left or right hand
"""


def count_fingers(results, image):
  fingerCount = 0
  imageHeight, imageWidth, _ = image.shape
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        hand_types = [hand_info.classification[0].label for hand_index, hand_info in
                      enumerate(results.multi_handedness)]
        thumb_tip = hand_landmarks.landmark[4]
        pinky_tip = hand_landmarks.landmark[20]
        if thumb_tip.x < pinky_tip.x and hand_types[0] == 'Right':
            normalizedLandmark = hand_landmarks.landmark[4]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                               normalizedLandmark.y, imageWidth,
                                                                               imageHeight)
            if pixelCoordinatesLandmark is not None:
              Thumb_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[6]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Index_Pip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[10]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Middle_Pip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[14]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Ring_Pip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[18]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Pinky_Pip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[5]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                         imageHeight)
            if pixelCoordinatesLandmark is not None:
              Index_Mcp_x = pixelCoordinatesLandmark[0]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[9]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[13]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[17]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[3]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Thumb_Ip_x = pixelCoordinatesLandmark[0]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[8]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                         imageHeight)
            if pixelCoordinatesLandmark is not None:
              Index_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[12]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Middle_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[16]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Ring_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[20]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                    imageHeight)
            if pixelCoordinatesLandmark is not None:
              Pinky_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              thmb_indx_diff = Thumb_Ip_x - Index_Mcp_x
            else:
                continue
            if Index_Pip_y < Middle_Tip_y and Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y:
              if Index_Tip_y < Middle_Pip_y and Index_Tip_y < Ring_Pip_y and Index_Tip_y < Pinky_Pip_y:
                fingerCount = 1
            if Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y:
              if Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y:
                fingerCount = 2
            if Index_Pip_y < Pinky_Tip_y and Middle_Pip_y < Pinky_Tip_y and Ring_Pip_y < Pinky_Tip_y:
              if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y:
                if Index_Tip_y < Thumb_Tip_y and Middle_Tip_y < Thumb_Tip_y and Ring_Tip_y < Thumb_Tip_y:
                  fingerCount = 3
            if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y:
              if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                fingerCount = 4
            if thmb_indx_diff < -15:
              if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                fingerCount = 5
        elif thumb_tip.x > pinky_tip.x and hand_types[0] == 'Left':
            normalizedLandmark = hand_landmarks.landmark[4]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                   normalizedLandmark.y, imageWidth,
                                                                                   imageHeight)
            if pixelCoordinatesLandmark is not None:
              Thumb_Tip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[6]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)

            if pixelCoordinatesLandmark is not None:
              Index_Pip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[10]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Middle_Pip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[14]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Ring_Pip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[18]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Pinky_Pip_y = pixelCoordinatesLandmark[1]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[5]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Index_Mcp_x = pixelCoordinatesLandmark[0]

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[9]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[13]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[17]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)

            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[3]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Thumb_Ip_x = pixelCoordinatesLandmark[0]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[8]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                         imageHeight)
            if pixelCoordinatesLandmark is not None:
              Index_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[12]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Middle_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[16]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Ring_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              normalizedLandmark = hand_landmarks.landmark[20]
              pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                     normalizedLandmark.y, imageWidth,
                                                                                     imageHeight)
            if pixelCoordinatesLandmark is not None:
              Pinky_Tip_y = pixelCoordinatesLandmark[1]
            if pixelCoordinatesLandmark is not None:
              thmb_indx_diff = Thumb_Ip_x - Index_Mcp_x
            else:
              continue
            if Index_Pip_y < Middle_Tip_y and Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y:
              if Index_Tip_y < Middle_Pip_y and Index_Tip_y < Ring_Pip_y and Index_Tip_y < Pinky_Pip_y:
                fingerCount = 1
            if Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y:
              if Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y:
                fingerCount = 2
            if Index_Pip_y < Pinky_Tip_y and Middle_Pip_y < Pinky_Tip_y and Ring_Pip_y < Pinky_Tip_y:
              if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y:
                if Index_Tip_y < Thumb_Tip_y and Middle_Tip_y < Thumb_Tip_y and Ring_Tip_y < Thumb_Tip_y:
                  fingerCount = 3
            if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y:
                if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                    fingerCount = 4
            if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y:
              if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                fingerCount = 5
            if thmb_indx_diff < 15:
              if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                fingerCount = 4
  return fingerCount
