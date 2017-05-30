# Forrest Weatherby
# efw5xb

# Flipping an image
from cImage import *

# Open an image
old_image = FileImage('uva.gif')

# Open a window that is twice the size of the original image
my_image_window = ImageWin("Image Processing", old_image.width * 2, old_image.height)

# Draw the image on the window
old_image.draw(my_image_window)

# Create a new, blank image
new_image = EmptyImage(old_image.width, old_image.height)

# For each pixel in the original image...
for row in range(old_image.height):
    for col in range(old_image.width):
        # ... get the original pixel ...
        oldPixel = old_image.getPixel(col, row)

        # ... and draw it in the opposite place in the new image
        new_image.setPixel(row, col, oldPixel)

# Make sure to put the new image over to the side the right number of pixels
new_image.setPosition(old_image.width + 1, 0)

# Draw the new image
new_image.draw(my_image_window)

# Wait for a user to click the window to close the image
my_image_window.exitOnClick()