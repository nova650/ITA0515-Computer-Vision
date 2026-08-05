from PIL import Image

img = Image.open("C:/Users/ASUS/OneDrive/Documents/computer vision/Bheem.jpg")
gray = img.convert("L")

img.show()
gray.show()

gray.save("grayscale_image.jpg")
