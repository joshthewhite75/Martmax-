from PIL import Image
import os

path = r'c:\Users\Josh\Projects\martmax-redesign\logo.png'
img = Image.open(path).convert('RGBA')
pixels = img.load()
width, height = img.size
# find bounding box of non-transparent pixels
minx, miny, maxx, maxy = width, height, 0, 0
for y in range(height):
    for x in range(width):
        if pixels[x, y][3] != 0:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
if maxx < minx or maxy < miny:
    print('Image is fully transparent?')
else:
    cropped = img.crop((minx, miny, maxx + 1, maxy + 1))
    cropped.save(path)
    print('Cropped image from', img.size, 'to', cropped.size, 'saved', path)
