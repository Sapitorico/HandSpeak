#!/usr/bin/python3
import cv2
import mediapipe as mp
import numpy as np
import onnxruntime as ort

mp_hands = mp.solutions.hands

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "HAND",
            "I", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class PreprocessImage:

    def __init__(self, imgSize=None):
        self.offset = 10
        self.imgSize = imgSize

    @staticmethod
    def Hands_model_configuration(image_mode, max_hand, complexity):
        hands = mp_hands.Hands(
            static_image_mode=image_mode,
            max_num_hands=max_hand,
            model_complexity=complexity,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        return hands

    @staticmethod
    def Hands_detection(image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        result = model.process(image)
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, result

    @staticmethod
    def Detect_hand_type(hand_type, results, positions, copie_img):
        """
        tracking of the position of the hand in the image, depending on the image chosen by the user

        hand_type: Left or Right hand type
        results: detection results
        positions: list of positions
        copie_img: copy image

        return: position of the hand
        """
        for hand_index, hand_info in enumerate(results.multi_handedness):
            hand_types = hand_info.classification[0].label
            if hand_types == hand_type:
                PreprocessImage.get_position(positions, results, copie_img)
            if hand_type == "all":
                PreprocessImage.get_position(positions, results, copie_img)
            return positions

    @staticmethod
    def get_position(positions, results, copie_img):
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                alto, ancho, c = copie_img.shape
                positions.append((lm.x * ancho, lm.y * alto, lm.z * ancho))

    def Draw_Bound_Boxes(self, positions, frame, cls=""):
        """
        hand box

        positions: Position array
        frame: Frame
        """
        x_min, y_min, x_max, y_max, width, height = PreprocessImage.get_ejes(positions);
        x1, y1 = x_min, y_min
        x2, y2 = x_min + width, y_min + height
        if y1 - self.offset - 15 >= 0 and y2 - self.offset + 40 <= frame.shape[
            0] and x1 - self.offset - 40 >= 0 and x2 - self.offset + 50 <= \
                frame.shape[1]:
            cv2.rectangle(frame, (x1 - self.offset - 40, y1 - self.offset - 15),
                          (x2 - self.offset + 50, y2 - self.offset + 40),
                          (0, 255, 0), 3)
            cv2.putText(frame, f'{cls}', (x1 - self.offset - 40, y1 - self.offset - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.60, [225, 255, 255], thickness=1)

    def Get_image_resized(self, positions, copie_image):
        """
        image reshaping

        positions: x y z coordinates
        copie_img: copy frame

        return: redeemed image
        """
        alto, ancho, c = copie_image.shape
        x_min, y_min, x_max, y_max, width, height = PreprocessImage.get_ejes(positions)
        centro_x, centro_y = int((x_min + x_max) / 2), int((y_min + y_max) / 2)
        lado = max(width, height)
        x1 = max(0, centro_x - int(lado / 2) - 50)
        y1 = max(0, centro_y - int(lado / 2) - 50)
        ancho = min(ancho - x1, int(lado) + 100)
        alto = min(alto - y1, int(lado) + 100)
        x2, y2 = x1 + ancho, y1 + alto
        resized_hand = copie_image[y1:y2, x1:x2]
        resized_hand = cv2.resize(resized_hand, (self.imgSize, self.imgSize), interpolation=cv2.INTER_CUBIC)
        return resized_hand

    @staticmethod
    def get_ejes(positions):
        x_min = int(min(positions, key=lambda x: x[0])[0])
        y_min = int(min(positions, key=lambda x: x[1])[1])
        x_max = int(max(positions, key=lambda x: x[0])[0])
        y_max = int(max(positions, key=lambda x: x[1])[1])
        width = x_max - x_min
        height = y_max - y_min
        return x_min, y_min, x_max, y_max, width, height


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
