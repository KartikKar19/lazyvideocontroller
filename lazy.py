import cv2
import mediapipe as mp
import pyautogui
import time

def count_active_fingers(hand_landmarks):
    finger_count = 0
    threshold = (hand_landmarks.landmark[0].y * 100 - hand_landmarks.landmark[9].y * 100) / 2

    if (hand_landmarks.landmark[5].y * 100 - hand_landmarks.landmark[8].y * 100) > threshold:
        finger_count += 1

    if (hand_landmarks.landmark[9].y * 100 - hand_landmarks.landmark[12].y * 100) > threshold:
        finger_count += 1

    if (hand_landmarks.landmark[13].y * 100 - hand_landmarks.landmark[16].y * 100) > threshold:
        finger_count += 1

    if (hand_landmarks.landmark[17].y * 100 - hand_landmarks.landmark[20].y * 100) > threshold:
        finger_count += 1

    if (hand_landmarks.landmark[5].x * 100 - hand_landmarks.landmark[4].x * 100) > 6:
        finger_count += 1

    return finger_count


video_capture = cv2.VideoCapture(0)

drawing_utils = mp.solutions.drawing_utils
hand_detection = mp.solutions.hands
hand_tracker = hand_detection.Hands(max_num_hands=1)

initial_time_set = False
previous_finger_count = -1

while True:
    current_time = time.time()
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)

    result = hand_tracker.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        finger_count = count_active_fingers(hand_landmarks)

        if previous_finger_count != finger_count:
            if not initial_time_set:
                initial_time = time.time()
                initial_time_set = True

            elif (current_time - initial_time) > 0.2:
                if finger_count == 1:
                    pyautogui.press("right")

                elif finger_count == 2:
                    pyautogui.press("left")

                elif finger_count == 3:
                    pyautogui.press("up")

                elif finger_count == 4:
                    pyautogui.press("down")

                elif finger_count == 5:
                    pyautogui.press("space")

                previous_finger_count = finger_count
                initial_time_set = False

        drawing_utils.draw_landmarks(frame, hand_landmarks, hand_detection.HAND_CONNECTIONS)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        video_capture.release()
        break
