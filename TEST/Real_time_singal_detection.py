#!/usr/bin/python
import cv2
import os
import numpy as np
# from tensorflow.keras.utils import load_img, img_to_array
import torch
from tensorflow.keras.saving import load_model
from Base_Model.Detection_tools import Base_Model
from ultralytics import YOLO
from torchvision.models import video
import torchvision.transforms as transforms
import tensorflow as tf
model = YOLO("CNN_Model/models/epoch-63.pt")
# print(model)


# modelo = "CNN_Model/Modelo/Modelo1.h5"
# peso = "CNN_Model/pesos/pesos1.h5"
#
# direction = "mp_datasets"
# dire_img = os.listdir(direction
# )
# cnn = load_model(modelo)  # Cargamos el modelo
# cnn.load_weights(peso)  # Cargamos los pesos
#
DATA_PATH = 'mp_dataset'
actions = []
imgSize = 224
size_data = 1000
save_frequency = 10
hand_type = "Right"
key = 0
count = 0

Base = Base_Model(DATA_PATH, actions, imgSize, size_data)
Hands = Base.Hands_model_configuration(False, 1, 1)
# #
# # predictions = []
# # threshold = 0.5
#
capture = cv2.VideoCapture(0)

# with hands as Hands:
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
            result = model.predict(resized_hand, show=True)
    if key == 27:
        exit(0)
    cv2.imshow("image capture", frame)
capture.release()
cv2.destroyAllWindows()

