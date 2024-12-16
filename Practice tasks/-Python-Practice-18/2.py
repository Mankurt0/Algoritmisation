from PIL import Image

img = Image.open("screen_camera.png")
img = img.rotate(180)
img.save("screen_camera.png")