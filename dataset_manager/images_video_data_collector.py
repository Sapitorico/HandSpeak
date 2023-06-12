#!/usr/bin/python3
"""
con este archivo se pueden extraer todas las imagenes
de manos de todos los videos que esten en el mismo
directorio que este archivo

este depende del modulo utils
"""
import cv2
from utils import Utils
import os

def Image_Collection(id_cam, DATA_PATH, action, imgSize, size_data, num_hands, hand_type):
    capture = cv2.VideoCapture(id_cam)
    Base = Utils(DATA_PATH, action, imgSize, size_data)
    Hands = Base.Hands_model_configuration(False, num_hands, 1)
    #key = 0
    #k = 0
    count = 0
    with Hands:
        while capture.isOpened():
            #key = cv2.waitKey(1)
            success, image = capture.read()
            if not success:
                return
            image = cv2.flip(image, 1)
            image, result = Base.Hands_detection(image, Hands)
            copy_image = image.copy()
            if result.multi_hand_landmarks:
                positions = []
                positions =  Base.Detect_hand_type(hand_type, result, positions, copy_image)
                if len(positions) != 0:
                    Base.Draw_Bound_Boxes(positions, image, hand_type)
                    resized_hand = Base.Get_image_resized(positions, copy_image)
                    #if key == 115:
                    #    k = 1
                    #if k == 1:
                    Base.Save_resized_hand(resized_hand, count, hand_type)
                    count += 1
            #if key == 27:
            #    break
            cv2.imshow("image capture", image)
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    # Obtener la lista de vídeos en el directorio actual
    video_directory = "."  # Puedes cambiar el directorio si es necesario
    video_files = [f for f in os.listdir(video_directory) if f.endswith(".mp4")]
    print(video_files)

    
    DATA_PATH = "img_test_all"
    imagSize = 224
    size_data = 2000
    num_hands = 1
    hand_type = "Left"

    for video_file in video_files:
        id_cam = os.path.join(video_directory, video_file)
        action = [id_cam[2]]
        print(id_cam[2])
        #extract_frames(video_path, video_directory, frames_per_second)
        Image_Collection(id_cam, DATA_PATH, action, imagSize, size_data, num_hands, hand_type)
