import sys
from PIL import Image, ImageOps

#handling file errors
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].lower().endswith(".jpg") and not sys.argv[1].lower().endswith("jpeg") and sys.argv[2].lower().endswith(".jpg") and not sys.argv[2].lower().endswith("jpeg"):
    sys.exit("Invalid input")
first_1, last_1 = sys.argv[1].split(".")
first_2, last_2 = sys.argv[2].split(".")
if last_1 != last_2:
    sys.exit("Input and output have different extensions")

try:
#trying to open image file PIL.Image.open(fp, mode='r', formats=None)
    muppet = Image.open(sys.argv[1]
#trying open pasting image
    shirt = Image.open("shirt.png")

#trying resizing image PIL.ImageOps.fit(image, size, method=Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    muppet_resize = ImageOps.fit(muppet, shirt.size)

#trying pasting other image Image.paste(im, box=None, mask=None)[source]
# no need    box = (muppet_resize.width - shirt.width, muppet_resize.height - shirt.height)
    muppet_resize.paste(shirt, mask = shirt)

#trying save the image Image.save(fp, format=None, **params)[source]
    muppet_resize.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File doesn't exist")
