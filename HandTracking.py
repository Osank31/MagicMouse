import cv2
import mediapipe as mp
import HandDetectorModule as hdm
from pynput.mouse import Button, Controller
mouse = Controller()

cap = cv2.VideoCapture(1)
detector = hdm.HandDetector()

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = detector.findHands(frame)
    lmList=detector.findHandLandmarkCoordinates(frame,0)

    if len(lmList)!=0:
        x_window = lmList[4][1]
        y_window = lmList[4][2]
        x_screen = (1280/510)*(x_window-50)
        y_screen = (1080/375)*(y_window-45)
        mouse.position=(x_screen, y_screen)
        index_finger_coordinates_window = (x_window, y_window)
        thumb_coordinates_window = (lmList[8][1], lmList[8][2])
        diffrence = (abs(index_finger_coordinates_window[0]-thumb_coordinates_window[0]),abs(index_finger_coordinates_window[1]-thumb_coordinates_window[1]))
        if diffrence[1]<=15:
            print("Click ", diffrence)
            mouse.click(Button.left, 1)

    cv2.imshow("h", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()