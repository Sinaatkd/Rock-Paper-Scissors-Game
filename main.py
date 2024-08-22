import cv2

from hand_tracker import HandTracker
from hand_gesture_recognizer import HandGestureRecognizer
from game import Game

hand_detection = HandTracker()
hand_gesture_recognizer = HandGestureRecognizer()


cap = cv2.VideoCapture(0)
is_hand_detected = False

game = Game()
is_user_want_play_again = False


frame_rate = cap.get(cv2.CAP_PROP_FPS)
frame_count = 0


def put_text(frame, text, position):
    # Font settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (0, 0, 255)  # BGR => Black color
    cv2.putText(frame, text, position, font, font_scale, font_color, font_thickness)


def show_info():
    put_text(frame, f"Your Chose: {game.user_choice}", (30, 100))
    put_text(frame, f"Computer Chose: {game.computer_choice}", (30, 140))
    put_text(frame, f"your score: {game.user_score}", (30, y-20))
    put_text(frame, f"computer score: {game.computer_score}", (30, y-60))
    put_text(frame, f"Draw: {game.draw_count}", (30, y-100))

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    y, x, _ = frame.shape
    put_text(frame, f"Remaining rounds: {game.remaining_round}", (30, 40))

    if not is_hand_detected and not is_user_want_play_again:
        put_text(frame, "Wait For Detecting Your Hand", (int(x / 2) - 250, int(y / 2)))

    # processing on frame to detect hand
    result_hand = hand_detection.process(frame)

    # draw landmarks
    hand_detection.draw_hand_landmarks(frame, result_hand)

    if result_hand.multi_hand_landmarks:
        is_hand_detected = True

        if game.playing() or is_user_want_play_again:
            frame_count += 1
            frame_timestamp_ms = (frame_count / frame_rate) * 1000

        if game.playing():
            # put text in center
            put_text(frame, f"{int(frame_timestamp_ms / 1000)}", (int(x / 2), int(y / 2)))
        else:
            # put text in center
            put_text(frame, f"{game.get_result()}", (int(x / 2) - 80, int(y / 2)))
            put_text(frame, f"Do You Want to Play again? 1) yes 2) no", (int(x / 2) - 350, int(y / 2) + 40))
            put_text(frame, f"{int(frame_timestamp_ms / 1000)}", (int(x / 2), int(y / 2) + 80))
            is_user_want_play_again = True
        
        
        user_choice = ''
        landmark = result_hand.multi_hand_landmarks[0].landmark
        if hand_gesture_recognizer.is_hand_paper_mode(landmark):
            user_choice = "paper"
        elif hand_gesture_recognizer.is_hand_rock_mode(landmark):
            user_choice = "rock"
        elif hand_gesture_recognizer.is_hand_scissors_mode(landmark):
            user_choice = "scissors"
        else:
            pass

        # run this code 3 seconds after hand detected
        if game.playing() and frame_timestamp_ms >= 3000:
            game.ready()
            game.set_user_choice(user_choice)
            game_result = game.play()
            frame_count = 0
            frame_timestamp_ms = 0
        
        if is_user_want_play_again and frame_timestamp_ms >= 3000:
            frame_count = 0
            if hand_gesture_recognizer.is_one_sign(landmark):
                game.reset()
            else:
                break

    else:
        is_hand_detected = False
        frame_count = 0 # reset timer

    show_info()
    cv2.imshow('window', frame)

    # close window when q key clicked
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
