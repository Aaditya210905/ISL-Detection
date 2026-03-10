import cv2
import numpy as np

def image_process(image, hands):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    return hands.process(image)


def keypoint_extraction(results):
    def process(hand):
        if not hand:
            return np.zeros(21 * 3)

        landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark])
        landmarks -= landmarks[0]  # wrist-relative
        return landmarks.flatten()

    # MediaPipe Holistic returns `left_hand_landmarks`/`right_hand_landmarks`.
    # MediaPipe Hands returns `multi_hand_landmarks` (+ optional `multi_handedness`).
    if hasattr(results, "left_hand_landmarks") or hasattr(results, "right_hand_landmarks"):
        lh = process(getattr(results, "left_hand_landmarks", None))
        rh = process(getattr(results, "right_hand_landmarks", None))
        return np.concatenate([lh, rh])  # (126,)

    lh = np.zeros(21 * 3)
    rh = np.zeros(21 * 3)

    multi_hand_landmarks = getattr(results, "multi_hand_landmarks", None)
    if not multi_hand_landmarks:
        return np.concatenate([lh, rh])

    multi_handedness = getattr(results, "multi_handedness", None)

    for idx, hand_landmarks in enumerate(multi_hand_landmarks):
        side = None
        if multi_handedness and idx < len(multi_handedness):
            try:
                side = multi_handedness[idx].classification[0].label
            except Exception:
                side = None

        vec = process(hand_landmarks)
        if side == "Left":
            lh = vec
        elif side == "Right":
            rh = vec
        else:
            # Fallback when handedness isn't available: fill first empty slot.
            if not np.any(lh):
                lh = vec
            elif not np.any(rh):
                rh = vec

    return np.concatenate([lh, rh])  # (126,)
