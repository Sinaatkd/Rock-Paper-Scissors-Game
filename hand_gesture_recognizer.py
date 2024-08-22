import cv2
import mediapipe as mp

from utils import calculate_angle

class HandGestureRecognizer:
    def __init__(self):
            self.mp_hands = mp.solutions.hands

    def is_hand_paper_gesture(self, landmark):
        index_finger_mcp = [
            landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP.value].x,
            landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP.value].y,
        ]
        index_finger_pip = [
            landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP.value].x,
            landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP.value].y,
        ]
        index_finger_dip = [
            landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP.value].x,
            landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP.value].y,
        ]
        index_finger_angle = calculate_angle(index_finger_mcp, index_finger_pip,
                                            index_finger_dip)
        
        middle_finger_mcp = [
            landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP.value].x,
            landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP.value].y,
        ]
        middle_finger_pip = [
            landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP.value].x,
            landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP.value].y,
        ]
        middle_finger_dip = [
            landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP.value].x,
            landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP.value].y,
        ]
        middle_finger_angle = calculate_angle(middle_finger_mcp, middle_finger_pip,
                                                middle_finger_dip)

        ring_finger_mcp = [
            landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP.value].x,
            landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP.value].y,
        ]
        ring_finger_pip = [
            landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP.value].x,
            landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP.value].y,
        ]
        ring_finger_dip = [
            landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP.value].x,
            landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP.value].y,
        ]
        ring_finger_angle = calculate_angle(ring_finger_mcp, ring_finger_pip,
                                            ring_finger_dip)

        pinky_mcp = [
            landmark[self.mp_hands.HandLandmark.PINKY_MCP.value].x,
            landmark[self.mp_hands.HandLandmark.PINKY_MCP.value].y,
        ]
        pinky_pip = [
            landmark[self.mp_hands.HandLandmark.PINKY_PIP.value].x,
            landmark[self.mp_hands.HandLandmark.PINKY_PIP.value].y,
        ]
        pinky_dip = [
            landmark[self.mp_hands.HandLandmark.PINKY_DIP.value].x,
            landmark[self.mp_hands.HandLandmark.PINKY_DIP.value].y,
        ]
        pinky_angle = calculate_angle(pinky_mcp, pinky_pip, pinky_dip)

        angles = [index_finger_angle,middle_finger_angle,ring_finger_angle,pinky_angle]

        
        if min(angles) > 100:
            return True
        return False
        