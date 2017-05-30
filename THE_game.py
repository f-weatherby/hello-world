# Forrest Weatherby
# efw5xb

import pygame
import gamebox
import math

camera = gamebox.Camera(800, 600)
player = gamebox.from_image(50, 50)
speed = 5
bullet_list = []
x = 0
def tick(keys):
    global speed
    global x
    camera.clear("cyan")
    if pygame.K_UP in keys:
        player.y -= speed
    if pygame.K_DOWN in keys:
        player.y += speed
    if pygame.K_RIGHT in keys:
        player.x += speed
    if pygame.K_LEFT in keys:
        player.x -= speed
    if pygame.K_d in keys:
        player.rotate(-6)
        x += 5
    if pygame.K_a in keys:
        player.rotate(6)
        x -= 5
    if pygame.K_w in keys:
        bullet_list.append(gamebox.from_color(player.x, player.y, "yellow", 5, 5))
    for bullet in bullet_list:
        y = math.radians(x)
        bullet.y += math.sin(y)*5
        bullet.x += math.cos(y)*5
        if bullet.x > 810 or bullet.x < -10:
            bullet_list.remove(bullet)
        elif bullet.y > 610 or bullet.y < -10:
            bullet_list.remove(bullet)
        camera.draw(bullet)
    camera.draw(player)
    camera.display()
ticks_per_second = 60
gamebox.timer_loop(ticks_per_second, tick)