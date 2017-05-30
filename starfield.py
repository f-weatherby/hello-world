# Forrest Weatherby
# efw5xb

# A starfield simulation.

import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)
stars = []
counter = 0

def tick(keys):
    global counter
    counter += 1

    if counter % 5 == 0:
        numstars = random.randint(0,7)
        for i in range(numstars):
            stars.append(gamebox.from_color(random.randint(5,795),0,"white",3,3))

    camera.clear("black")

    for star in stars:
        # move the star
        star.y += 3
        if(star.y > 600):
            stars.remove(star)
        # draw the star
        camera.draw(star)

    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)