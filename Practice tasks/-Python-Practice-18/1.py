from PIL import Image

img = Image.open("screenshot.jpg")
img = img.convert("L")
img.save("screenshot_bw.jpg")