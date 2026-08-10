import cv2

img = cv2.imread("Sample.jpg")

cv2.namedWindow("Original Image")
cv2.imshow("Original Image", img)
cv2.moveWindow("Original Image", 200, 200)
cv2.waitKey(0)
cv2.destroyAllWindows()
