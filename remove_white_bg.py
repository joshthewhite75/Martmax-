from PIL import Image
import os

path = r'c:\Users\Josh\Projects\martmax-redesign\logo.png'
if not os.path.exists(path):
    raise FileNotFoundError(path)
img = Image.open(path)
img = img.convert('RGBA')
width, height = img.size
pixels = img.load()
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 0 and r > 240 and g > 240 and b > 240:
            pixels[x, y] = (255, 255, 255, 0)
img.save(path)
print('Saved transparent logo:', path)
