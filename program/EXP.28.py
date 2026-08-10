import cv2
import numpy as np

img = cv2.imread("Sample.jpg")
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened_img = cv2.filter2D(img, -1, kernel)

cv2.imshow("Input Image", img)
cv2.imshow("Convolutional Image", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
