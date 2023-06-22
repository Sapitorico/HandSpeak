#!/usr/bin/env python
# -*- coding: utf-8 -*-
import onnxruntime as ort
import onnx
import numpy as np

"""
This class is used to load the model and make predictions, functionalities:
The Model_Loader class is responsible for loading an ONNX model, preprocessing input images, and making predictions based on the loaded model. It also handles the retrieval of class names from the model metadata and the configuration of the ONNX runtime session.

Methods:
- __init__(self, threshold, model_path): initializes the class by loading the ONNX model from the specified path, retrieving class names from the model metadata, and configuring the ONNX runtime session.
- get_output_names(self): returns the names of the model's output nodes.
- preprocess_image(self, resized_hand): preprocesses the input image by normalizing its pixel values and transposing its dimensions.
- predict(self, resized_hand): preprocesses the input image, runs it through the loaded model, and returns the predicted class label.

Fields:
- alphabet: a list of class names retrieved from the model metadata.
- threshold: a threshold value used to filter out low-confidence predictions.
- opt_session: an ONNX runtime session options object used to configure the session.
- ort_session: an ONNX runtime inference session object used to run the loaded model.
- input_names: a list of the names of the model's input nodes.
- output_names: a list of the names of the model's output nodes.
"""


class ModelLoader:

    def __init__(self, threshold, model_path="../models/alfabetov3.onnx"):
        try:
            model = onnx.load(model_path)
            metadata_props = model.metadata_props
            classes = None
            for prop in metadata_props:
                if prop.key == 'names':
                    classes = eval(prop.value)
                    break
            self.alphabet = [classes[i] for i in range(len(classes))]

            self.threshold = threshold
            self.opt_session = ort.SessionOptions()
            self.opt_session.enable_mem_pattern = True
            self.opt_session.enable_cpu_mem_arena = True
            self.opt_session.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

            # Verificar disponibilidad de GPU y ajustar proveedores de ejecución
            if ort.get_device() == 'GPU':
                EP_list = ['CUDAExecutionProvider']
            else:
                EP_list = ['CPUExecutionProvider']

            self.ort_session = ort.InferenceSession(model_path, providers=EP_list)
            model_inputs = self.ort_session.get_inputs()
            self.input_names = [input.name for input in model_inputs]
            model_output = self.ort_session.get_outputs()
            self.output_names = [output.name for output in model_output]
        except Exception as e:
            raise Exception("Error al cargar el modelo: {}".format(str(e)))

    def get_output_names(self):
        return self.output_names

    def preprocess_image(self, resized_hand):
        input_image = resized_hand / 255.0
        input_image = input_image.transpose(2, 0, 1)
        return input_image

    def predict(self, resized_hand):
        try:
            input_image = self.preprocess_image(resized_hand)
            input_tensor = np.expand_dims(input_image, axis=0).astype(np.float32)
            outputs = self.ort_session.run(self.get_output_names(), {self.input_names[0]: input_tensor})[0]
            predictions = np.squeeze(outputs).T
            scores = np.max(predictions[:, 4:], axis=1)
            predictions = predictions[scores > self.threshold, :]
            scores = scores[scores > self.threshold]
            class_ids = np.argmax(predictions[:, 4:], axis=-1)
            cls = ""
            for score, class_id in zip(scores, class_ids):
                cls_id = int(class_id)
                cls = self.alphabet[cls_id]
                if cls == "nie":
                    cls = "Ñ"
            return cls
        except Exception as e:
            raise Exception("Error al realizar la predicción: {}".format(str(e)))


if __name__ == "__main__":
    import cv2
    from image_processing import HandDetectionUtils
    """
    test in real time
    """
    capture = cv2.VideoCapture(0)
    Base = HandDetectionUtils(1,224)
    model = ModelLoader(0.8)
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
            if key == 27:
                break
            cv2.imshow("image capture", image)
    capture.release()
    cv2.destroyAllWindows()