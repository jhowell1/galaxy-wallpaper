from PIL import Image, ImageDraw, ImageFont
import random

#1920x1080

background = Image.new('RGB', (1440, 900), color = (0,0,0))

fnt = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 8)

d = ImageDraw.Draw(background)

for i in range(0,1440):

    for j in range(0,900):

        randInt = random.randint(1,1001)

        if j < 324 and randInt > 999:
            d.text((i,j), ".", font = fnt, fill = (255,255,255))
        elif j >= 324 and j < 648 and randInt > 996:
            d.text((i,j), ".", font=fnt, fill=(255, 255, 255))
        elif j >= 648 and j < 756 and randInt > 995:
            d.text((i,j), ".", font=fnt, fill=(255, 255, 255))
        else:
            if randInt > 996:
                d.text((i, j), ".", font=fnt, fill=(255, 255, 255))

background.save('galaxy_pixels_mom.png')
