from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")

#filtered_image = img.filter(ImageFilter.CONTOUR)

converted_image = img.convert("L")

converted_image.save("greyscale.png", "png")

#filtered_image.save("contour.png", "png")

# print(img.mode)