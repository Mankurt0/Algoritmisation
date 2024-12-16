from PIL import ImageDraw, Image

pixels = [[0,1,1,1,1,1,1,1,0],
          [1,0,1,1,1,1,1,0,1],
          [1,1,1,0,0,0,1,1,1],
          [1,1,0,1,0,1,0,1,1],
          [1,1,0,0,1,0,0,1,1],
          [1,1,0,1,0,1,0,1,1],
          [1,1,1,0,0,0,1,1,1],
          [1,0,1,1,1,1,1,0,1],
          [0,1,1,1,1,1,1,1,0]]
img = Image.new("RGB", (9,9), "white")
draw = ImageDraw.Draw(img)
for y, row in enumerate(pixels):
    for x, pixel in enumerate(row):
        if pixel == 1:
            color = "black"
        else:
            color = "white"
        draw.rectangle((x,y,x,y), fill=color)
img.save("my pixel pict.png")