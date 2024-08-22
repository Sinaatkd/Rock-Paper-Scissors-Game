import mediapipe as mp


class HandTracker:
    def __init__(self, max_num_hands=1, min_detection_confidence=0.50, min_tracking_confidence=0.50) -> None:
        # Initialize MediaPipe Hand module and other utilities
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def process(self, frame):
        result = self.mp_hands.process(frame)
        return result

    def draw_hand_landmarks(self, frame, result_hand):
        """Draw pose landmarks and connections on the detected hand."""
        if result_hand.multi_hand_landmarks:
            for hand_landmarks in result_hand.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )

    