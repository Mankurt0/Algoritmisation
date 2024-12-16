from PIL import Image

img = Image.open("figures.png")
img = img.crop((271, 123, 476, 401))
img.save("cube.png")