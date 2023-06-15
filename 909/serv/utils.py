#!/usr/bin/python3
import cv2
import mediapipe as mp
import os
import numpy as np
import onnxruntime as ort

# Inicializar el modelo de detección de manos
mp_hands = mp.solutions.hands

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "HAND",
            "I", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


class Utils:
    def __init__(self, imgSize=None):
        self.imgSize = imgSize
        self.offset = 10

    @staticmethod
    def Hands_model_configuration(image_mode, max_hand, complexity):
        hands = mp_hands.Hands(
            static_image_mode=image_mode,
            max_num_hands=max_hand,
            model_complexity=complexity,
            min_detection_confidence=0.1,
            min_tracking_confidence=0.1
        )
        return hands

    @staticmethod
    def Hands_detection(image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        result = model.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, result

    @staticmethod
    def Detect_hand_type(hand_type, results, positions, copie_img):
        """
        tracking of the position of the hand in the image, depending on the image chosen by the user

        :param hand_type: Left or Right hand type
        :param results: detection results
        :param positions: list of positions
        :param copie_img: copy image

        return: position of the hand
        """
        for hand_index, hand_info in enumerate(results.multi_handedness):
            hand_types = hand_info.classification[0].label
            if hand_types == hand_type:
                for hand_landmarks in results.multi_hand_landmarks:
                    for id, lm in enumerate(hand_landmarks.landmark):
                        alto, ancho, c = copie_img.shape
                        positions.append((lm.x * ancho, lm.y * alto, lm.z * ancho))       
        return positions

    def Get_image_resized(self, positions, copie_img):
        """
        image reshaping

        :param positions: x y z coordinates
        :param copie_img: copy frame

        return: redeemed image
        """
        alto, ancho, c = copie_img.shape
        x_min = int(min(positions, key=lambda x: x[0])[0])
        y_min = int(min(positions, key=lambda x: x[1])[1])
        x_max = int(max(positions, key=lambda x: x[0])[0])
        y_max = int(max(positions, key=lambda x: x[1])[1])
        width = x_max - x_min
        height = y_max - y_min
        centro_x, centro_y = int((x_min + x_max) / 2), int((y_min + y_max) / 2)
        # Calcular las coordenadas del cuadro centrado en la mano
        lado = max(width, height)
        x1 = max(0, centro_x - int(lado / 2) - 50)
        y1 = max(0, centro_y - int(lado / 2) - 50)
        ancho = min(ancho - x1, int(lado) + 100)
        alto = min(alto - y1, int(lado) + 100)
        x2, y2 = x1 + ancho, y1 + alto
        resized_hand = copie_img[y1:y2, x1:x2]
        resized_hand = cv2.resize(resized_hand, (self.imgSize, self.imgSize), interpolation=cv2.INTER_CUBIC)
        return resized_hand
    
class Model_loader:
    def __init__(self, model_path, threshold):
        model_path = model_path
        self.threshold = threshold
        self.opt_session = ort.SessionOptions()
        self.opt_session.enable_mem_pattern = False
        self.opt_session.enable_cpu_mem_arena = False
        self.opt_session.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
        EP_list = ['CUDAExecutionProvider', 'CPUExecutionProvider']
        self.ort_session = ort.InferenceSession(model_path, providers=EP_list)
        model_inputs = self.ort_session.get_inputs()
        self.input_names = [model_inputs[i].name for i in range(len(model_inputs))]
        model_output = self.ort_session.get_outputs()
        self.output_names = [model_output[i].name for i in range(len(model_output))]

    def output_names(self):
        return self.output_names

    def predict(self, resized_hand):
        input_image = resized_hand / 255.0
        input_image = input_image.transpose(2, 0, 1)
        input_tensor = input_image[np.newaxis, :, :, :].astype(np.float32)
        outputs = self.ort_session.run(self.output_names, {self.input_names[0]: input_tensor})[0]
        predictions = np.squeeze(outputs).T
        scores = np.max(predictions[:, 4:], axis=1)
        predictions = predictions[scores > self.threshold, :]
        scores = scores[scores > self.threshold]
        class_ids = np.argmax(predictions[:, 4:], axis=1)
        cls = ""
        for score, class_id in zip(scores, class_ids):
            cls_id = int(class_id)
            cls = alphabet[cls_id]
        return cls