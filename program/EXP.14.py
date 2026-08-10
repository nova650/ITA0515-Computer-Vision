import cv2
import numpy as np

img = cv2.imread("Sample.jpg")
rows, cols = img.shape[:2]

src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
dst_points = np.float32([[0, 0], [cols - 1, 0], [0, int(0.7 * rows)], [cols - 1, int(0.7 * rows)]])

M, _ = cv2.findHomography(src_points, dst_points)
homography_img = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Homography Transformed", homography_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
