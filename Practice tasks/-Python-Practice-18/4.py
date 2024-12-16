from PIL import ImageDraw, Image, ImageFont

img = Image.new("RGB", (200, 200), "cyan")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", size=20)
draw.text((25, 90), "Mankurt0 was here", font=font)
img.save("Mankurt0 was here.png")