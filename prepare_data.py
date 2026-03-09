import os
import cv2
import numpy as np
import mediapipe as mp
from my_functions import image_process, keypoint_extraction

DATASET_PATH = "dataset"

X, y = [], []

labels = sorted([d for d in os.listdir(DATASET_PATH)
                 if os.path.isdir(os.path.join(DATASET_PATH, d))])

label_map = {label: idx for idx, label in enumerate(labels)}
print("Labels:", label_map)

mp_hands = mp.solutions.hands

with mp_hands.Hands(static_image_mode=True) as hands:
    for label in labels:
        folder = os.path.join(DATASET_PATH, label)
        for img_name in os.listdir(folder):
            img_path = os.path.join(folder, img_name)
            image = cv2.imread(img_path)
            if image is None:
                continue

            image = cv2.resize(image, (640, 480))
            results = image_process(image, hands)
            keypoints = keypoint_extraction(results)

            if np.sum(keypoints) == 0:
                continue

            X.append(keypoints)
            y.append(label_map[label])

X = np.array(X)
y = np.array(y)

# per-sample normalization
X = X / np.linalg.norm(X, axis=1, keepdims=True)

np.save("X.npy", X)
np.save("y.npy", y)

print("Saved:", X.shape)
