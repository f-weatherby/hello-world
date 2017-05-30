# Forrest Weatherby
# efw5xb

from cImage import *

# Here we define a method that will take a pixel
# and return a pixel that is "flipped" as far as RGB is concerned
def negative_pixel(old_pixel):
    new_red = 255 - old_pixel.getRed()
    new_green = 255 - old_pixel.getGreen()
    new_blue = 255 - old_pixel.getBlue()
    new_pixel = Pixel(new_red, new_green, new_blue)
    return new_pixel

# Open an image
old_image = FileImage('uva.gif')

# Open a window that is twice the size of the original image
image_window = ImageWin("Image Processing", old_image.width * 2, old_image.height)

# Draw the image on the window
old_image.draw(image_window)

# Create a new, blank image
new_image = EmptyImage(old_image.width, old_image.height)

# For each pixel in the original image...
for row in range(old_image.height):
    for col in range(old_image.width):
        # ... get that pixel ...
        old_pixel = old_image.getPixel(col, row)
        # ... flip the pixel ...
        new_pixel = negative_pixel(old_pixel)
        # ... and put that pixel in the new image
        new_image.setPixel(col, row, new_pixel)

# Make sure to put the new image over to the side the right number of pixels
new_image.setPosition(old_image.width + 1, 0)

# Draw the new image
new_image.draw(image_window)

# Wait for a user to click the window to close the image
image_window.exitOnClick()