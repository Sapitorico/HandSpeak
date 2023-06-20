from fastapi import FastAPI
from starlette.websockets import WebSocket
from aux_functions import processLetter, processNumber
from image_processing import HandDetectionUtils
import json
import numpy as np
import cv2
import urllib.request
from YOLO_model_loader import YOLO_loader

model = YOLO_loader(0.8)
Base = HandDetectionUtils(1, 224)
Hands = Base.hands

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    checker = "sapo"
    while True:
        json_data = await websocket.receive_text()
        data = json.loads(json_data)
        req = urllib.request.urlopen(data[0])
        arr_img = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr_img, -1)

        if data[2] == "Letter":
            to_predict = processLetter(image, data[1])
            if to_predict != "Error, not a hand":
                result = model.predict(to_predict)
                if result != checker and result != "":
                    checker = result
                    await websocket.send_text(result)
            else:
                if checker != "sapo":
                    checker = "sapo"
                    await websocket.send_text("")
        if data[2] == "Number":
           result = processNumber(image)
           if result != "Error, not a hand" and result != checker:
               checker = result
               await websocket.send_text(str(result))