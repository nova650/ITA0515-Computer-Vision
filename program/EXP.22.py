import cv2
import numpy as np

image = cv2.imread("Sample.jpg")
kernel = np.array([[0, 1, 0], [1, -8, 1], [0, 1, 0]])
sharpened = cv2.filter2D(image, -1, kernel)

cv2.imshow("Original", image)
cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
