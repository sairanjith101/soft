import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

if(cap.isOpened == False):
    print("Error! Webcam not open")

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()