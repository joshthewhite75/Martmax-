from PIL import Image, ImageDraw, ImageFont
import os

# Open the original logo
original = Image.open('images/martmax logo.jpeg')

# Convert to RGBA
if original.mode != 'RGBA':
    original = original.convert('RGBA')

# Remove white background
data = original.getdata()
new_data = []
for item in data:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
original.putdata(new_data)

# Create a large favicon first (256x256)
favicon_large = Image.new('RGBA', (256, 256), (255, 255, 255, 0))

# Resize logo to fit nicely on the canvas
logo_resized = original.resize((220, 220), Image.Resampling.LANCZOS)

# Calculate position to center the logo
x = (256 - 220) // 2
y = (256 - 220) // 2

# Paste logo
favicon_large.paste(logo_resized, (x, y), logo_resized)

# Save full size
favicon_large.save('images/favicon.png', 'PNG')
print('✓ Created: favicon.png (256x256)')

# Create optimized smaller versions
favicon_32 = favicon_large.resize((32, 32), Image.Resampling.LANCZOS)
favicon_32.save('images/favicon-32x32.png', 'PNG')
print('✓ Created: favicon-32x32.png')

favicon_16 = favicon_large.resize((16, 16), Image.Resampling.LANCZOS)
favicon_16.save('images/favicon-16x16.png', 'PNG')
print('✓ Created: favicon-16x16.png')

# Also create an ICO file for better browser support
favicon_large.save('images/favicon.ico', 'ICO')
print('✓ Created: favicon.ico (for better browser support)')

print('\n✅ All favicons updated! Refresh your browser cache (Ctrl+Shift+Delete)')
