from PIL import Image, ImageFilter


image = Image.open(r"/Users/altynai/Desktop/PycharmProjects/geekapp/contacts/images/dnm.png")

print(image.size)

blurred = image.filter(ImageFilter.BLUR)
image.show()
blurred.show()


new_image = image.resize((500, 200))
# new_image.save("new_image500.png")
new_image.show()

image_cropped = image.crop((177, 882, 1179, 1707))
image_cropped.show()


img = image.filter(ImageFilter.CONTOUR)
img.show()
