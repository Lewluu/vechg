from cgitb import reset
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.7)
mp_draw = mp.solutions.drawing_utils

model = load_model('src/HandGestureDetection/mp_hand_gesture')

f = open('src/HandGestureDetection/gesture.names', 'r')
class_names = f.read().split('\n')

f.close()
print(class_names)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    x, y, c = frame.shape

    if ret is not True:
        print("Failed to load camera ...")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    class_name = ''

    if result.multi_hand_landmarks:
        landmarks = []
        for hands_lms in result.multi_hand_landmarks:
            for lm in hands_lms.landmark:
                lm_x = int(lm.x * x)
                lm_y = int(lm.y * y)

                landmarks.append([lm_x, lm_y])

            mp_draw.draw_landmarks(frame, hands_lms, mp_hands.HAND_CONNECTIONS)
        
        prediction = model.predict([landmarks])
        print(prediction)
        class_id = np.argmax(prediction)
        class_name = class_names[class_id]

        cv2.putText(frame, class_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("vechg", frame)
    if cv2.waitKey(1) == 27:    break

cap.release()
cv2.destroyAllWindows()