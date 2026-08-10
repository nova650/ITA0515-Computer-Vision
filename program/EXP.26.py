import cv2

img = cv2.imread("Sample.jpg")
h, w = img.shape[:2]

logo = cv2.resize(img, (int(w * 0.2), int(h * 0.2)))
lh, lw = logo.shape[:2]

roi = img[h - lh - 10 : h - 10, w - lw - 10 : w - 10]
blended = cv2.addWeighted(roi, 0.6, logo, 0.4, 0)
img[h - lh - 10 : h - 10, w - lw - 10 : w - 10] = blended

cv2.putText(img, "WATERMARK", (50, h - 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
