# Forrest Weatherby, Phil Head, Diva C.
# efw5xb, aph8tb, dc5zd

# our first game
import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
character = gamebox.from_color(50, 100, "black", 40, 40)
coin = gamebox.from_color(400, 200, "yellow", 15, 15)
chicken = gamebox.from_color(400, 300, "green", 40, 40)
health_bar_label = gamebox.from_text(400, 16, "HEALTH", "arial", 20, "red")
x = 100
touch_times = 0
ground = gamebox.from_color(-100, 600, "black", 2000, 10)
wall_1 = gamebox.from_color(800, 100, "black", 10, 2000)
wall_2 = gamebox.from_color(50, 3, "black", 1500, 5)
wall_3 = gamebox.from_color(3, 3, "black", 5, 1500)
wall_list = [ground, wall_2, wall_1, wall_3]
time = 6000
score = 0
start = False

def tick(keys):
    global time, score, start, x, touch_times
    camera.clear("light blue")
    seconds = str(int((time / ticks_per_second))).zfill(3)
    time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, "arial", 24, "white")
    score_box = gamebox.from_text(75, 30, "Score: " + str(score), "arial", 24, "white")
    if pygame.K_SPACE in keys:
        start = True
    if start == True:
        time -= 1
        if chicken.x < character.x:
            chicken.x += 2.3
        else:
            chicken.x -= 2.3
        if chicken.y < character.y:
            chicken.y += 2.3
        else:
            chicken.y -= 2.3
        if coin.touches(character):
            coin.x = random.randint(10, 800)
            coin.y = random.randint(10, 600)
            score += 1
    elif start == False:
        start_message = gamebox.from_text(400, 100, "Avoid the green box and collect coins. Press space to start the game.", "times new roman", 23, "black")
    if pygame.K_RIGHT in keys:
        character.x += 4
    if pygame.K_LEFT in keys:
        character.x -= 4
    for i in wall_list:
        if character.touches(i):
            character.move_to_stop_overlapping(i)
            character.yspeed = 0
    if character.touches(chicken):
        touch_times += 1
        x -= 10
        chicken.center = [-30, -30]
    if pygame.K_UP in keys:
        character.y -= 4
    if pygame.K_DOWN in keys:
        character.y += 4
    camera.draw(time_box)
    camera.draw(score_box)
    camera.draw(gamebox.from_color(400, 50, "red", x, 50))
    camera.draw(health_bar_label)
    camera.draw(character)
    camera.draw(chicken)
    camera.draw(coin)
    camera.draw(wall_3)
    camera.draw(wall_1)
    camera.draw(wall_2)
    camera.draw(ground)
    if start == False:
        camera.draw(start_message)
    if touch_times >= 10:
        camera.draw(gamebox.from_text(400, 300, "GAME OVER!", "arial", 50, "white"))
        camera.draw(gamebox.from_text(400, 400, "Your score: " + str(score), "arial", 30, "white"))
        if score <= 20:
            camera.draw(gamebox.from_text(400, 450, "Eh...disappointing", "arial", 20, "white"))
        else:
            camera.draw(gamebox.from_text(400, 450, "hmmm...not bad", "arial", 20, "white"))
        gamebox.pause()
    if seconds == 0:
        camera.draw(gamebox.from_text(400, 300, "YOU WIN!", "arial", 50, "white"))
        camera.draw(gamebox.from_text(400, 400, "Your score: " + str(score), "arial", 30, "white"))
        camera.draw(gamebox.from_text(400, 400, "Congradulations you survived to the end!", "arial", 30, "white"))
        gamebox.pause()
    camera.display()
ticks_per_second = 50

gamebox.timer_loop(ticks_per_second, tick)