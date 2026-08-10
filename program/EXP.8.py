import cv2

img = cv2.imread("Sample.jpg")
height, width = img.shape[:2]

bigger_image = cv2.resize(img, (int(width * 1.5), int(height * 1.5)))
smaller_image = cv2.resize(img, (int(width * 0.5), int(height * 0.5)))

cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
