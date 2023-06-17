from image_processing import mp_drawing


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
