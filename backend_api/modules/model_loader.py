#!/usr/bin/env python
# -*- coding: utf-8 -*-
import onnxruntime as ort
import numpy as np

"""
This class is used to load the model and make predictions, functionalities:
The Model_loader class is responsible for loading a pre-trained model and making predictions on input images of hand gestures. It preprocesses the input image, runs it through the loaded model, and returns the predicted class of the hand gesture.

Methods:
- __init__(self, threshold): initializes the class by setting the threshold for the prediction score, setting the session options for the loaded model, and loading the model using onnxruntime. It also retrieves the input and output names of the model.
- output_names(self): returns the output names of the loaded model.
- preprocess_image(self, resized_hand): preprocesses the input image by normalizing it and transposing the dimensions.
- predict(self, resized_hand): preprocesses the input image, runs it through the loaded model, and returns the predicted class of the hand gesture.

Fields:
- model_path: the path to the pre-trained model.
- alphabet: a list of strings representing the classes of hand gestures.
- threshold: the minimum score required for a predicted class to be considered valid.
- opt_session: session options for the loaded model.
- ort_session: the loaded model.
- input_names: the names of the input nodes of the loaded model.
- output_names: the names of the output nodes of the loaded model.
"""


class Model_loader:
    model_path = "../model/epoch-63.onnx"
    alphabet = ["A", "B", "C", "D", "E", "enie", "F", "G", "H", "HAND",
                "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def __init__(self, threshold):
        self.threshold = threshold
        self.opt_session = ort.SessionOptions()
        self.opt_session.enable_mem_pattern = False
        self.opt_session.enable_cpu_mem_arena = False
        self.opt_session.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
        EP_list = ['CUDAExecutionProvider', 'CPUExecutionProvider']
        self.ort_session = ort.InferenceSession(Model_loader.model_path, providers=EP_list)
        model_inputs = self.ort_session.get_inputs()
        self.input_names = [input.name for i, input in enumerate(model_inputs)]
        model_output = self.ort_session.get_outputs()
        self.output_names = [output.name for i, output in enumerate(model_output)]


    def output_names(self):
        return self.output_names

    def preprocess_image(self, resized_hand):
        input_image = resized_hand / 255.0
        input_image = input_image.transpose(2, 0, 1)
        return input_image

    def predict(self, resized_hand):
        input_image = self.preprocess_image(resized_hand)
        input_tensor = np.expand_dims(input_image, axis=0).astype(np.float32)
        # input_tensor = input_image[np.newaxis, :, :, :].astype(np.float32)
        # input_tensor = input_image[np.newaxis, :, :, :].astype(np.float32)
        outputs = self.ort_session.run(self.output_names, {self.input_names[0]: input_tensor})[0]
        predictions = np.squeeze(outputs).T
        scores = np.max(predictions[:, 4:], axis=1)
        predictions = predictions[scores > self.threshold, :]
        scores = scores[scores > self.threshold]
        class_ids = np.argmax(predictions[:, 4:], axis=-1)
        cls = ""
        for score, class_id in zip(scores, class_ids):
            cls_id = int(class_id)
            cls = Model_loader.alphabet[cls_id]
        return cls


if __name__ == "__main__":
    import cv2
    from image_processing import HandDetectionUtils
    """
    test in real time
    """
    capture = cv2.VideoCapture(0)
    Base = HandDetectionUtils(1,224)
    model = Model_loader(0.05)
    Hands = Base.hands
    with Hands:
        while capture.isOpened():
            key = cv2.waitKey(1)
            success, image = capture.read()
            if not success:
                continue
            image = cv2.flip(image, 1)
            result = Base.detect_hands(image)
            copy_image = image.copy()
            if result.multi_hand_landmarks:
                positions = Base.detect_hand_type("Right", result, copy_image)
                if len(positions) != 0:
                    resized_hand = Base.get_image_resized(positions, copy_image)
                    cls = model.predict(resized_hand)
                    print(cls)
                    cv2.imshow("hola", resized_hand)
            if key == 27:
                break
            cv2.imshow("image capture", image)
    capture.release()
    cv2.destroyAllWindows()