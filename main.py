import cv2
from hand_tracker import HandTracker


hand_detection = HandTracker()


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # processing on frame to detect hand
    result_hand = hand_detection.process(frame)

    # draw landmarks
    hand_detection.draw_hand_landmarks(frame, result_hand)

    cv2.imshow('window', frame)

    # close window when q key clicked
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
