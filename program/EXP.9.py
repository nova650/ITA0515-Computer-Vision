import cv2

img = cv2.imread("Sample.jpg")

rotated_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_ccw = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("Rotated CW", rotated_cw)
cv2.imshow("Rotated CCW", rotated_ccw)
cv2.waitKey(0)
cv2.destroyAllWindows()
