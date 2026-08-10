from PIL import Image, ImageFilter

im1 = Image.open("Sample.jpg")
im2 = im1.filter(ImageFilter.UnsharpMask(radius=3, percent=200, threshold=5))
im2.show()
