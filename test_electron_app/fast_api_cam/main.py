import cv2
import base64
from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketState
from utils.utils import PreprocessImage, Model_loader

app = FastAPI()


@app.websocket("/ws")
async def video(websocket: WebSocket):
    await websocket.accept()
    await Real_time_sign_detection(websocket)

# Lógica de detección de señas en tiempo real
async def Real_time_sign_detection(websocket: WebSocket):
    model = Model_loader("models/best (2).onnx", 0.8)
    hand_type = "Right"
    utils = PreprocessImage(224)
    Hands = utils.Hands_model_configuration(False, 1, 1)
    capture = cv2.VideoCapture(0)

    with Hands:
        while websocket.client_state != WebSocketState.DISCONNECTED:
            success, image = capture.read()
            if not success:
                continue
            image = cv2.flip(image, 1)
            image, results = utils.Hands_detection(image, Hands)
            copy_image = image.copy()
            cls = ""
            if results.multi_hand_landmarks:
                positions = utils.Detect_hand_type(hand_type, results, [], copy_image)
                if len(positions) != 0:
                    resized_hand = utils.Get_image_resized(positions, copy_image)
                    cls = model.predict(resized_hand)
                    utils.Draw_Bound_Boxes(positions, image, cls)
            _, buffer = cv2.imencode(".jpg", image)
            frame_bytes = buffer.tobytes()
            frame_base64 = base64.b64encode(frame_bytes).decode("utf-8")

            data = {
                "image": frame_base64,
                "cls": cls
            }

            try:
                await websocket.send_json(data)
            except Exception:
                break

