from fastapi import FastAPI
from starlette.websockets import WebSocket
from images_data_collector import process, url_to_image
from PIL import Image
from utils import Model_loader

model = Model_loader('C:/Users/5771/Desktop/909/serv/models/best (2).onnx', 0.1)

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        image = url_to_image(data)
        to_predict = process(image, 224, 1, "Right")
        if to_predict != "sapo":
            result = model.predict(to_predict)
            await websocket.send_text(result)
