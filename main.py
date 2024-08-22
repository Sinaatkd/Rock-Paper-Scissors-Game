import mediapipe as mp
import cv2

from hand_tracker import HandTracker
from hand_gesture_recognizer import HandGestureRecognizer

hand_detection = HandTracker()
hand_gesture_recognizer = HandGestureRecognizer()


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # processing on frame to detect hand
    result_hand = hand_detection.process(frame)

    # draw landmarks
    hand_detection.draw_hand_landmarks(frame, result_hand)

    if result_hand.multi_hand_landmarks:
        landmark = result_hand.multi_hand_landmarks[0].landmark
        if hand_gesture_recognizer.is_hand_paper_mode(landmark):
            print("paper")
        elif hand_gesture_recognizer.is_hand_rock_mode(landmark):
            print("Rock")
        else:
            print('unknown mode')

    cv2.imshow('window', frame)

    # close window when q key clicked
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
