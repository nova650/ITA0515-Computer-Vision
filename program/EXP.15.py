import cv2
import numpy as np

img = cv2.imread("Sample.jpg")
h, w = img.shape[:2]

pts_src = np.float32([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]])
pts_dst = np.float32([[50, 50], [w - 80, 20], [w - 30, h - 60], [20, h - 40]])

A = []
for (x, y), (xp, yp) in zip(pts_src, pts_dst):
    A.append([-x, -y, -1, 0, 0, 0, x * xp, y * xp, xp])
    A.append([0, 0, 0, -x, -y, -1, x * yp, y * yp, yp])

U, S, Vt = np.linalg.svd(np.array(A, dtype=np.float64))
H = Vt[-1].reshape(3, 3)
H = H / H[2, 2]

dlt_img = cv2.warpPerspective(img, H, (w, h))

cv2.imshow("Original", img)
cv2.imshow("DLT Transformed", dlt_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
