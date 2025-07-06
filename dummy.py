import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 1, self.detectionCon, self.trackCon)  # Include model_complexity (1 or 0)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():  # Check if the camera opened successfully
        print("Error: Could not open camera. Check camera connection and index.")
        return  # Exit if the camera couldn't be opened

    detector = handDetector()

    while True:
        success, img = cap.read()
        if not success:  # Check if a frame was read successfully
            print("Error: Could not read frame. Check camera input.")
            break  # Exit the loop if no frame was read

        img = detector.findHands(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)

        if cv2.waitKey(10) & 0xFF == 27:  # Check for ESC key press (important!)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()