#!/usr/bin/python3
import cv2
from utils import Utils

def Image_Collection(id_cam, DATA_PATH, action, imgSize, size_data, num_hands, hand_type):
    capture = cv2.VideoCapture(id_cam)
    Base = Utils(DATA_PATH, action, imgSize, size_data)
    Hands = Base.Hands_model_configuration(False, num_hands, 1)
    key = 0
    k = 0
    count = 0
    with Hands:
        while capture.isOpened():
            key = cv2.waitKey(1)
            success, image = capture.read()
            if not success:
                continue
            image = cv2.flip(image, 1)
            image, result = Base.Hands_detection(image, Hands)
            copy_image = image.copy()
            if result.multi_hand_landmarks:
                positions = []
                positions =  Base.Detect_hand_type(hand_type, result, positions, copy_image)
                if len(positions) != 0:
                    Base.Draw_Bound_Boxes(positions, image)
                    resized_hand = Base.Get_image_resized(positions, copy_image)
                    if key == 115:
                        k = 1
                    if k == 1:
                        Base.Save_resized_hand(resized_hand, count, hand_type)
                        count += 1
            if key == 27:
                break
            cv2.imshow("image capture", image)
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    id_cam = 0
    DATA_PATH = "images/Training1"
    action = ['A']
    imagSize = 224
    size_data = 100
    num_hands = 1
    hand_type = "Right"
    Image_Collection(id_cam, DATA_PATH, action, imagSize, size_data, num_hands, hand_type)
