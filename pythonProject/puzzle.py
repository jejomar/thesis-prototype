import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
        return lmlist

#def startTime():

def main():
    TIMER = int(5)
    cap = cv2.VideoCapture(0)
    width, height = 320, 240
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        cv2.imshow('Camera Feed', img)
        cv2.moveWindow('Camera Feed', 1215, 600)
        cv2.waitKey(1)

        if len(lmlist) != 0:

            prev = time.time()

            while TIMER >= 0:
                ret, img = cap.read()

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(TIMER), (260, 220), font,
                            2, (0, 0, 0),
                            2, cv2.LINE_AA)
                cv2.imshow('Camera Feed', img)
                cv2.waitKey(125)
                cur = time.time()

                if cur - prev >= 1:
                    prev = cur
                    TIMER = TIMER - 1

            else:
                ret, img = cap.read()
                cv2.imshow('Camera Feed', img)
                # time for which image displayed
                cv2.waitKey(1000)
                # Save the frame
                TIMER = int(5)

if __name__ == "__main__":
    main()