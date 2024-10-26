import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = int(maxHands)  # Ensure this is an int
        self.detectionCon = float(detectionCon)  # Should be a float
        self.trackCon = float(trackCon)  # Should be a float
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.output = self.hands.process(frameRGB)

        if self.output.multi_hand_landmarks:
            for handLms in self.output.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

        return frame

    def findHandLandmarkCoordinates(self, frame, handNo=0):
        lmList=[]
        if self.output.multi_hand_landmarks:
            myHand = self.output.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                h, w, _ = frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])

        return lmList

# def main():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Camera not found or cannot be opened.")
#         return
#
#     detector = HandDetector()
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame = cv2.flip(frame, 1)
#         frame = detector.findHands(frame)
#         lmList = detector.findHandLandmarkCoordinates(frame)
#
#         # if len(lmList)!=0:
#             # print(abs(lmList[8][1]-lmList[4][1]),abs(lmList[8][2]-lmList[4][2]))
#
#         cv2.imshow("HandDetector CAM", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()


# if __name__ == "__main__":
    # main()
