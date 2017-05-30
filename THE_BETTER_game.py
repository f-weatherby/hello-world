# Forrest Weatherby
# efw5xb

# Example of doing an animated sprite with a sprite sheet.

import pygame
import gamebox

camera = gamebox.Camera(800, 600)
sheet = gamebox.load_sprite_sheet("https://s3-us-west-2.amazonaws.com/s.cdpn.io/160783/smurf_sprite.png", 4, 4)
frame = 0
direction = 0
counter = 0
character = gamebox.from_image(70, 70, sheet[frame])
character.size = 50, 50
right = True


def tick1(keys):
    global frame
    global direction
    global counter
    global right
    if pygame.K_RIGHT in keys:
        if not right:
            character.flip()
        character.x += 4
        frame += 1
        character.image = sheet[frame]
        if frame == 15:
            frame = 0
        right = True
    if pygame.K_LEFT in keys:
        if right:
            character.flip()
        character.x -= 4
        frame += 1
        character.image = sheet[frame]
        if frame == 15:
            frame = 0
        right = False



    camera.clear("white")
    camera.draw(character)
    camera.display()


ticks_per_second = 20

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick1)
