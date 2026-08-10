import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    frame = cv2.imread("Sample.jpg")

rows, cols = frame.shape[:2]
src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
dst_points = np.float32([[0, 0], [cols - 1, 0], [int(0.33 * cols), rows - 1], [int(0.66 * cols), rows - 1]])

M = cv2.getPerspectiveTransform(src_points, dst_points)
dst = cv2.warpPerspective(frame, M, (cols, rows))

cv2.imshow("Original Frame", frame)
cv2.imshow("Transformed Frame", dst)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
