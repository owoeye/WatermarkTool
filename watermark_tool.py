# import all the libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from matplotlib import colors


def add_watermark(file, text, font_size, font_color):
    # image opening
    image = Image.open(file)

    # text Watermark
    watermark_image = image.copy()

    draw = ImageDraw.Draw(watermark_image)
    # ("font type",font size)
    w, h = image.size
    x, y = int(w / 2), int(h / 2)
    # if x > y:
    #     font_size = y
    # elif y > x:
    #     font_size = x
    # else:
    #     font_size = x

    font = ImageFont.truetype("arial.ttf", font_size)

    # add Watermark
    # (0,0,0)-black color text
    # convert color from float to int
    color = tuple(int(float(num)) for num in str(colors.to_rgb(font_color)).replace('(', '').replace(')', '').split(', '))
    draw.text((x, y), text, fill=color, font=font, anchor='ms')
    watermark_image.show()

