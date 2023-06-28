# !/usr/bin/python
# import cv2
# import math
# from Base_Model.HANDTrackingModule import HandDetector
from cvzone.HandTrackingModule import HandDetector
#
# cap = cv2.VideoCapture(0)
# detector = HandDetector(detectionCon=0.8, maxHands=2)
#
# while True:
#     success, frame = cap.read()
#     hands = detector.findHands(frame)
#
#     if hands and len(hands) == 2:
#         right_hand = None
#         left_hand = None
#
#         for hand in hands:
#             landmarks = hand['lmList']
#             handType = hand['type']
#
#             if handType == "Right":
#                 right_hand = hand
#             elif handType == "Left":
#                 left_hand = hand
#
#         if right_hand and left_hand:
#             thumb_tip_right = right_hand['lmList'][4]
#             index_finger_tip_right = right_hand['lmList'][8]
#             right_wrist = right_hand['lmList'][0]
#             left_index_finger = left_hand['lmList'][8]
#
#             cv2.line(frame, (right_wrist[0], right_wrist[1]), (left_index_finger[0], left_index_finger[1]),
#                      (0, 255, 0), 3)
#
#             # Contar dedos de la mano derecha
#             fingers_right = detector.fingersUp(right_hand)
#             if fingers_right in [[0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
#                 fingers_right_count = fingers_right.count(1)
#             else:
#                 fingers_right_count = 0
#             cv2.putText(frame, f"Dedos Derecha: {fingers_right_count} matriz: {fingers_right}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
#                         (255, 0, 0), 2)
#
#             # Contar dedos de la mano izquierda
#             fingers_left = detector.fingersUp(left_hand)
#             if fingers_left in [[0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
#                 fingers_left_count = fingers_left.count(1)
#             else:
#                 fingers_left_count = 0
#             cv2.putText(frame, f"Dedos Izquierda: {fingers_left_count} matriz: {fingers_left}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,
#                         (255, 0, 0), 2)
#             if fingers_right == [0, 0, 0, 0, 0]:
#                 distance = math.sqrt(
#                     (left_index_finger[0] - right_wrist[0]) ** 2 + (left_index_finger[1] - right_wrist[1]) ** 2)
#                 if distance < 10:
#                     print("sapardo")
#
#     cv2.imshow("Frame", frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


#-----------------------------------------------


# import cv2
# from Base_Model.Detection_tools import Base_Model
# from ultralytics import YOLO
# model = YOLO("CNN_Model/models/model_- 17 june 2023 17_08.pt")
#
#
# DATA_PATH = 'mp_dataset'
# actions = []
# imgSize = 224
# size_data = 1000
# save_frequency = 10
# hand_type = "all"
# key = 0
# count = 0
#
# Base = Base_Model(DATA_PATH, actions, imgSize, size_data)
# Hands = Base.Hands_model_configuration(False, 2, 1)
# capture = cv2.VideoCapture(0)
#
#
# sequence = []
# sequence_length = 10
# while capture.isOpened():
#     key = cv2.waitKey(1)
#     success, image = capture.read()
#     if not success:
#         continue
#     image = cv2.flip(image, 1)
#     frame, results = Base.Hands_detection(image, Hands)
#     copie_img = frame.copy()
#     if results.multi_hand_landmarks:
#         positions = []
#         positions, key_points = Base.Detect_hand_type(hand_type, results, positions, copie_img)
#         if len(positions) != 0:
#             Base.Draw_Bound_Boxes(positions, frame)
#             predicted_action = ""
#             resized_hand = Base.Get_bound_boxes(positions, copie_img)
#             prediction = model.predict(resized_hand, verbose=False, save=False, conf=0.8)
#             names = model.names
#             for result in prediction:
#                 try:
#                     boxes = result[0].boxes.numpy()
#                     for box in boxes:  # there could be more than one detection
#                         cls = box.cls[0]
#                         print(names[cls])
#                 except:
#                     continue
#     if key == 27:
#         exit(0)
#     cv2.imshow("image capture", frame)
# capture.release()
# cv2.destroyAllWindows()

import cv2
from Base_Model.Detection_tools import Base_Model
from ultralytics import YOLO

model = YOLO("CNN_Model/palabras_una_mano.pt")

DATA_PATH = 'mp_dataset'
actions = []
imgSize = 224
size_data = 1000
save_frequency = 10
hand_type = "all"
key = 0
count = 0

Base = Base_Model(DATA_PATH, actions, imgSize, size_data)
Hands = Base.Hands_model_configuration(False, 2, 1)
capture = cv2.VideoCapture(0)

sequence = []
sequence_length = 30

while capture.isOpened():
    key = cv2.waitKey(1)
    success, image = capture.read()

    if not success:
        continue

    image = cv2.flip(image, 1)
    frame, results = Base.Hands_detection(image, Hands)
    copie_img = frame.copy()

    if results.multi_hand_landmarks:
        positions = []
        positions, key_points = Base.Detect_hand_type(hand_type, results, positions, copie_img)

        if len(positions) != 0:
            Base.Draw_Bound_Boxes(positions, frame)
            predicted_action = ""
            resized_hand = Base.Get_bound_boxes(positions, copie_img)
            prediction = model.predict(resized_hand, verbose=False, save=False, conf=0.8)
            names = model.names

            word_sequence = []

            for result in prediction:
                try:
                    boxes = result[0].boxes.numpy()
                    for box in boxes:
                        cls = box.cls[0]
                        predicted_word = names[cls]
                        word_sequence.append(predicted_word)
                except:
                    continue

            if len(word_sequence) > sequence_length:
                word_sequence = word_sequence[-sequence_length:]

            if len(word_sequence) > 0:
                word_counts = {}
                for word in word_sequence:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

                most_common_word = max(word_counts, key=word_counts.get)
                last_word = word_sequence[-1]

                if last_word is not None and word_counts.get(last_word, 0) > word_counts.get(most_common_word, 0):
                    print("Detected word:", last_word)
                else:
                    print("Detected word:", most_common_word)
            else:
                print("No words detected.")
    if key == 27:
        exit(0)

    cv2.imshow("image capture", frame)

capture.release()
cv2.destroyAllWindows()
#
