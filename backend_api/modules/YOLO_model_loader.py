from ultralytics import YOLO

class YOLO_loader:
    model = YOLO("")

    def __init__(self, threshold):
        self.threshold = threshold

    def predict(self, resized_hand):
        cls = ""
        prediction = YOLO_loader.model.predict(resized_hand, verbose=False, save=False, conf=self.threshold)
        for result in prediction:
            boxes = result[0].boxes.numpy()
            for box in boxes:
                cls = box.cls[0]
        return cls