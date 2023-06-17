from fastapi import FastAPI
from starlette.websockets import WebSocket
from images_data_collector import processLetter, url_to_image, processNumber
from PIL import Image
from model_loader import Model_loader
import json
import numpy as np
from image_processing import HandDetectionUtils

model = Model_loader(0.05)
Base = HandDetectionUtils(1, 224)
Hands = Base.hands

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        json_data = await websocket.receive_text()
        data = json.loads(json_data)
        image = url_to_image(data[0])
        image = np.array(image)

        if data[2] == "Letter":
            to_predict = processLetter(image, data[1])
            if to_predict != "Error, not a hand":
                result = model.predict(to_predict)
                await websocket.send_text(result)
        if data[2] == "Number":
           result = processNumber(image)
           if result != "Error, not a hand":
               await websocket.send_text(str(result))
               
