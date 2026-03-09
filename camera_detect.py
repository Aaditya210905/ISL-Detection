import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
from my_functions import image_process, keypoint_extraction

model = load_model("alphabet_dense.h5")

labels = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        #frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (640, 480))

        results = image_process(frame, hands)
        keypoints = keypoint_extraction(results)

        multi_hand_landmarks = getattr(results, "multi_hand_landmarks", None)
        if multi_hand_landmarks:
            for hand_landmarks in multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

        if np.sum(keypoints) != 0:
            keypoints = keypoints / np.linalg.norm(keypoints)
            pred = model.predict(keypoints.reshape(1, 126), verbose=0)

            conf = np.max(pred)
            letter = labels[np.argmax(pred)]

            if conf > 0.75:
                cv2.putText(
                    frame,
                    f"{letter} ({conf:.2f})",
                    (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    4
                )

        cv2.imshow("Discrete Alphabet Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
