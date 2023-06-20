from ultralytics import YOLO

class YOLO_loader:

    def __init__(self, threshold):
        self.threshold = threshold
        self.model = YOLO("../models/modeloLSUalfabeto.pt")

    def predict(self, resized_hand):
        cls = ""
        prediction = self.model.predict(resized_hand, verbose=False, save=False, conf=self.threshold)
        names = self.model.names
        for result in prediction:
            if len(result) > 0:
                boxes = result[0].boxes.numpy()
                for box in boxes:
                    cls_id = box.cls[0]
                    cls = names[cls_id]
                    if cls == "nie":
                        cls = "Ñ"
        return cls
