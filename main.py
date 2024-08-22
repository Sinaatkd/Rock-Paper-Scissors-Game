import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


cap = cv2.VideoCapture(0)


def draw_hand_landmarks(frame, result_hand):
    """draw pose landmarks and connections

    Args:
        frame
        result_hand
    """
    if result_hand.multi_hand_landmarks:
        for hand_landmarks in result_hand.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())


with mp_hands.Hands(max_num_hands=1,
                    min_detection_confidence=0.75,
                    min_tracking_confidence=0.75) as detector:

    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # processing on frame to detect hand
        result_hand = detector.process(frame)

        # draw landmarks
        draw_hand_landmarks(frame, result_hand)

        cv2.imshow('window', frame)

        # close window when q key clicked
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    