import cv2

img = cv2.imread("Sample.jpg")
h, w = img.shape[:2]

crop_img = img[h // 4 : 3 * h // 4, w // 4 : 3 * w // 4]

canvas = img.copy()
ch, cw = crop_img.shape[:2]
canvas[0:ch, 0:cw] = crop_img

cv2.imshow("Original", img)
cv2.imshow("Cropped", crop_img)
cv2.imshow("Copy Paste", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
