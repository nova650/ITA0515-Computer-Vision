from PIL import Image, ImageFilter

img = Image.open("Bheem.jpg")
blur = img.filter(ImageFilter.GaussianBlur(5))

img.show()
blur.show()

blur.save("blur_image.jpg")
