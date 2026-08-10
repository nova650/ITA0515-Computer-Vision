import cv2

img = cv2.imread("Sample.jpg", 0)
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)

cv2.imshow("Original", img)
cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
