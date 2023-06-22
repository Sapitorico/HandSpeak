import cv2
import mediapipe as mp
import math


class HandDetector:
    """
    Finds Hands using the mediapipe library. Exports the landmarks
    in pixel format. Adds extra functionalities like finding how
    many fingers are up or the distance between two fingers. Also
    provides bounding box info of the hand found.
    """

    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, minTrackCon=0.5):
        """
        mode: In static mode, detection is done on each image: slower
        maxHands: Maximum number of hands to detect
        detectionCon: Minimum Detection Confidence Threshold
        minTrackCon: Minimum Tracking Confidence Threshold
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.minTrackCon)
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True, flipType=True):
        """
        Finds hands in a BGR image.
        img: Image to find the hands in.
        Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        allHands = []
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                myHand = {}
                ## lmList
                mylmList = []
                for id, lm in enumerate(handLms.landmark):
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

    def fingersUp(self, myHand):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """
        myHandType = myHand["type"]
        myLmList = myHand["lmList"]
        if self.results.multi_hand_landmarks:
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



if  __name__ == "__main__":
    import cv2
    import math


    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    while True:
        success, frame = cap.read()
        hands = detector.findHands(frame)

        if hands and len(hands) == 2:
            right_hand = None
            left_hand = None

            for hand in hands:
                landmarks = hand['lmList']
                handType = hand['type']

                if handType == "Right":
                    right_hand = hand
                elif handType == "Left":
                    left_hand = hand

            if right_hand and left_hand:
                thumb_tip_right = right_hand['lmList'][4]
                index_finger_tip_right = right_hand['lmList'][8]
                right_wrist = right_hand['lmList'][0]
                left_index_finger = left_hand['lmList'][8]

                cv2.line(frame, (right_wrist[0], right_wrist[1]), (left_index_finger[0], left_index_finger[1]),
                         (0, 255, 0), 3)
                # Contar dedos de la mano derecha
                fingers_right = detector.fingersUp(right_hand)

                fingers_left = detector.fingersUp(left_hand)
                if fingers_right == [0, 0, 0, 0, 0]:
                    distance = math.sqrt(
                        (left_index_finger[0] - right_wrist[0]) ** 2 + (left_index_finger[1] - right_wrist[1]) ** 2)
                    if distance < 10:
                        print("sapardo")
                print("no")

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()