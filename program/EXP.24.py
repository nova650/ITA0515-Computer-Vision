import cv2
import numpy as np

img = cv2.imread("Sample.jpg")
blurred = cv2.GaussianBlur(img, (5, 5), 1.0)
mask = cv2.subtract(img, blurred)
sharpened = cv2.addWeighted(img, 1.0, mask, 1.5, 0)

cv2.imshow("Original", img)
cv2.imshow("High-Boost Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
