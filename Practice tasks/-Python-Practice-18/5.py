from PIL import ImageDraw, Image

img = Image.open("pixels.png")
draw = ImageDraw.Draw(img)
draw.rectangle((23,151,51,229), fill="blue")
draw.rectangle((178,36,221,79), fill="red")
img.save("pixels_ready.png")