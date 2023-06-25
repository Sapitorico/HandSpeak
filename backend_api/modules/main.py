from fastapi import FastAPI
from starlette.websockets import WebSocket
from aux_functions import processLetter, processNumber
import json
import numpy as np
import cv2
import urllib.request
from model_loader import ModelLoader


model = ModelLoader(0.8)

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
        image = cv2.flip(image, 1)  


        if currentmode == "Letter":
            result = processLetter(image, data[1], currentmode)

        elif currentmode == "Number":
            result = processNumber(image, currentmode)


        if result == "Error, not a hand":
                if checker != "checker":
                    checker = "checker"
                    await websocket.send_text("")

        elif result in ["Number", "Word", "Letter"]:
                currentmode = result
                await websocket.send_text("Changeing mode")
        
        else:
            if type(result) is not str:
                result = model.predict(result)
            if result != checker and result != "":
                checker = result
                await websocket.send_text(result)



        """
        if currentmode == "Letter":
            to_predict = processLetter(image, data[1], currentmode)
            if to_predict == "Error, not a hand":
                if checker != "checker":
                    checker = "checker"
                    await websocket.send_text("")
            elif type(to_predict) is not str:
                result = model.predict(to_predict)
                if result != checker and result != "":
                    checker = result
                    await websocket.send_text(result)
            elif to_predict in ["Number", "Word"]:
                currentmode = to_predict
                await websocket.send_text("Changeing mode") 

        if currentmode == "Number":
            result = processNumber(image, currentmode)
            if result == "Error, not a hand" and result == checker:
                await websocket.send_text("")
            elif result in ["Letter", "Word"]:
               currentmode = result
               await websocket.send_text("Changeing mode")
            else:
               checker = result
               await websocket.send_text(str(result))
        """
