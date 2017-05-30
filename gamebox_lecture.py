# Forrest Weatherby
# efw5xb

import pygame
import gamebox
camera = gamebox.Camera(800, 600)
moving_box = gamebox.from_color(20, 550, "red", 20, 40)

def tick(keys): # wipe the world, update the state of it; games are flipbooks.
    camera.clear("blue")
    moving_box.x += 3
    camera.draw(moving_box)
    x = 4
    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick) #refresh the screen 30 times per second, doing what the function says

