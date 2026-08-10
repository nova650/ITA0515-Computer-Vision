import cv2

image = cv2.imread("Sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
gradient = cv2.subtract(gradient_x, gradient_y)
gradient = cv2.convertScaleAbs(gradient)

cv2.imshow("Original", gray)
cv2.imshow("Gradient Mask", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
