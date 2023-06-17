from fastapi import FastAPI
from starlette.websockets import WebSocket
from images_data_collector import process, url_to_image
from PIL import Image
from utils import Model_loader
import json

model = Model_loader('./models/best (2).onnx', 0.1)

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        json_data = await websocket.receive_text()
        data = json.loads(json_data)
        image = url_to_image(data[0])
        to_predict = process(image, 224, 1, data[1])
        if to_predict != "Error, no hay mano":
            result = model.predict(to_predict)
            await websocket.send_text(result)
