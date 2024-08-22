import cv2

from time import sleep

from hand_tracker import HandTracker
from hand_gesture_recognizer import HandGestureRecognizer
from game import Game

hand_detection = HandTracker()
hand_gesture_recognizer = HandGestureRecognizer()


cap = cv2.VideoCapture(0)
is_hand_detected = False

game = Game()


# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
font_color = (0, 0, 0)  # Black color

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    y, x, _ = frame.shape

    if not is_hand_detected:
        cv2.putText(frame, "Wait For Detecting Your Hand", (int(x / 2), 40), font, font_scale, font_color, font_thickness)

    # processing on frame to detect hand
    result_hand = hand_detection.process(frame)

    # draw landmarks
    hand_detection.draw_hand_landmarks(frame, result_hand)

    if result_hand.multi_hand_landmarks:
        is_hand_detected = True

        game.ready()

        user_choice = ''
        landmark = result_hand.multi_hand_landmarks[0].landmark
        if hand_gesture_recognizer.is_hand_paper_mode(landmark):
            user_choice = "paper"
        elif hand_gesture_recognizer.is_hand_rock_mode(landmark):
            user_choice = "rock"
        elif hand_gesture_recognizer.is_hand_scissors_mode(landmark):
            user_choice = "scissors"
        else:
            continue
        game.set_user_choice(user_choice)
        cv2.putText(frame, f"Your Chose: {user_choice}", (30, 40), font, font_scale, font_color, font_thickness)
        cv2.putText(frame, f"Computer Chose: {game.computer_choice}", (30, 100), font, font_scale, font_color, font_thickness)
        game_result = game.play()

    else:
        is_hand_detected = False

    cv2.imshow('window', frame)

    # close window when q key clicked
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
