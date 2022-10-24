import cv2
import mediapipe as mp

class WebCam:
    def __init__(self):
        self._cap = cv2.VideoCapture(0)
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands()
        self._mp_draw = mp.solutions.drawing_utils
        self._finger_coords = [(8, 6, "index finger"), (12, 10, "middle finger"), (16, 14, "ring finger"), (20, 18, "pinky finger")]
        self._thumb_coord = (4, 2, "thumb")
    
    def Run(self):
        while True:
            success, image = self._cap.read()
            image = cv2.flip(image, 1)

            if not success:
                print("Failed to load video capture ...")
                break

            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self._hands.process(rgb)
            multi_land_marks = results.multi_hand_landmarks

            if multi_land_marks:
                hand_list = []

                for hand_lms in multi_land_marks:
                    self._mp_draw.draw_landmarks(image, hand_lms, self._mp_hands.HAND_CONNECTIONS)
                    
                    for idx, lm in enumerate(hand_lms.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        hand_list.append((cx, cy))
                
                for point in hand_list:
                    cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
                    fingers_showing = []

                    for coord in self._finger_coords:
                        if hand_list[coord[0]][1] < hand_list[coord[1]][1]:
                            fingers_showing.append(coord[2])
                    if hand_list[self._thumb_coord[0]][0] > hand_list[self._thumb_coord[1]][0]:
                        fingers_showing.append(self._thumb_coord[2])
                
                h = 50
                for finger in fingers_showing:
                    cv2.putText(image, finger, (15, h), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    h += 50

            cv2.imshow("VECHG Window", image)
            if cv2.waitKey(1) == 27:    break
    
    def Exit(self):
        self._cap.release()
        cv2.destroyAllWindows()
    

