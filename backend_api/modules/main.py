from fastapi import FastAPI
from starlette.websockets import WebSocket
from aux_functions import processLetter, processNumber
#from image_processing import HandDetectionUtils
import json
import numpy as np
import cv2
import urllib.request
from model_loader import ModelLoader
#from control_hand import HandControl

model = ModelLoader(0.8)
#control = HandControl()
app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    checker = "checker"
    currentmode = "Letter"
    await websocket.accept()
    while True:
        json_data = await websocket.receive_text()
        data = json.loads(json_data)
        req = urllib.request.urlopen(data[0])
        arr_img = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr_img, -1)
    

       # with Hands:
        #    result = base.detect_hands(image)
         #   if result.multi_hand_landmarks:
          #      currentmode = control.change_mode(image, result, currentmode)


        if data[2] == "Letter":
            to_predict = processLetter(image, data[1])
            if to_predict != "Error, not a hand":
                result = model.predict(to_predict)
                if result != checker and result != "":
                    checker = result
                    await websocket.send_text(result)
            else:
                if checker != "checker":
                    checker = "checker"
                    await websocket.send_text("")

        if data[2] == "Number":
           result = processNumber(image)
           if result != "Error, not a hand" and result != checker:
               checker = result
               await websocket.send_text(str(result))