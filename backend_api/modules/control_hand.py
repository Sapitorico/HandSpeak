#!/usr/bin/python3
import math


class Hand_control:
    def __init__(self):
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []

    def findHands(self, img, results=None, flipType=True,):
        """
        Finds hands in a BGR image.
        img: Image to find the hands in.
        Image with or without drawings
        """
        allHands = []
        h, w, c = img.shape
        if results.multi_hand_landmarks:
            for handType, handLms in zip(results.multi_handedness, results.multi_hand_landmarks):
                myHand = {}
                mylmList = []
                for lm in handLms.landmark:
                    px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                    mylmList.append([px, py, pz])

                myHand["lmList"] = mylmList

                if flipType:
                    if handType.classification[0].label == "Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:
                    myHand["type"] = handType.classification[0].label
                allHands.append(myHand)
        return allHands




    def fingersUp(self, myHand, results):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """

        myHandType = myHand["type"]
        myLmList = myHand["lmList"]
        if results.multi_hand_landmarks:
            fingers = []
            # Thumb
            if myHandType == "Right":
                if myLmList[self.tipIds[0]][0] > myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.tipIds[0]][0] < myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipIds[id]][1] < myLmList[self.tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers


    def change_mode(self, image, result):
        hands = self.findHands(image, result, True)

        if hands and len(hands) == 2:
            right_hand = None
            left_hand = None

            for hand in hands:
                handType = hand['type']

                if handType == "Right":
                    right_hand = hand
                elif handType == "Left":
                    left_hand = hand

            if right_hand and left_hand:
                right_wrist = right_hand['lmList'][0]
                left_index_finger = left_hand['lmList'][8]

                cv2.line(image, (right_wrist[0], right_wrist[1]), (left_index_finger[0], left_index_finger[1]),
                         (0, 255, 0), 3)
                # Contar dedos de la mano derecha
                fingers_right = self.fingersUp(right_hand, result)
                if fingers_right == [0, 0, 0, 0, 0]:
                    distance = math.sqrt(
                        (left_index_finger[0] - right_wrist[0]) ** 2 + (left_index_finger[1] - right_wrist[1]) ** 2)
                    if distance < 10:
                        return True
            return False


if __name__ == "__main__":
    import cv2
    from image_processing import HandDetectionUtils

    """
    test in real time
    """
    capture = cv2.VideoCapture(0)
    Base = HandDetectionUtils(224)
    Hands = Base.hands
    control = Hand_control()
    with Hands:
        while capture.isOpened():
            key = cv2.waitKey(1)
            success, image = capture.read()
            if not success:
                continue
            image = cv2.flip(image, 1)
            result = Base.detect_hands(image)
            if result.multi_hand_landmarks:
                if control.change_mode(image, result):
                    print("change mode")
                else:
                    print("")
            if key == 27:
                break
            cv2.imshow("image capture", image)
    capture.release()
    cv2.destroyAllWindows()