from PIL import Image

img = Image.open('logo.png').convert('RGBA')
w, h = img.size
pix = img.load()
minx, miny, maxx, maxy = w, h, 0, 0
for y in range(h):
    for x in range(w):
        if pix[x, y][3] != 0:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
print('size', w, h)
print('bbox', minx, miny, maxx + 1, maxy + 1)
print('crop size', maxx - minx + 1, maxy - miny + 1)
