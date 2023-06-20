from fastapi import FastAPI
from starlette.websockets import WebSocket
from aux_functions import processLetter, processNumber
from model_loader import Model_loader
from image_processing import HandDetectionUtils
import json
import numpy as np
import cv2
import urllib.request

model = Model_loader(0.1)
Base = HandDetectionUtils(1, 224)
Hands = Base.hands

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
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
                await websocket.send_text(result)
        if data[2] == "Number":
           result = processNumber(image)
           if result != "Error, not a hand":
               await websocket.send_text(str(result))