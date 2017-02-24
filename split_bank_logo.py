from PIL import Image
import re
import os

im = Image.open('small_logo_sprite.png')

# The css style is copied from Alipay.com
with open('small_logo_sprite.css') as f:
    sprites = f.read().split('.ui-banklogo-s-')[1:]

logo_folder = os.path.join(os.path.curdir, 'small_logo')
if not os.path.exists(logo_folder):
    os.mkdir(logo_folder)

for s in sprites:
    m = re.match(('([a-zA-Z0-9]+)\{width:(\d+)px;'
              'height:(\d+)px;'
              'background-position:(-?\d+)(?:px)? (-?\d+)(?:px)?;\}'),
             s)
    matches = m.groups()
    # We need height/width and cordinate to identify each logo.
    bankname = matches[0]
    (width, height, x, y) = list(map(lambda x: abs(int(x)), matches[1:]))

    # top-left is the origin point.
    logo = im.crop((x, y, x+width, y+height))
    logo.save(os.path.join(logo_folder, "{}.png".format(bankname)))
