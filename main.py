import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    cv2.imshow('window', frame)

    # close window when q key clicked
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    