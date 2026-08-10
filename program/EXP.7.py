import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    frame = cv2.imread("Sample.jpg")

slow_frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
fast_frame = cv2.resize(frame, None, fx=2.0, fy=2.0)

cv2.imshow("Original", frame)
cv2.imshow("Slow Motion", slow_frame)
cv2.imshow("Fast Motion", fast_frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
