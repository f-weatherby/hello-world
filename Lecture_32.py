# Forrest Weatherby
# efw5xb

# jumping puzzle game - pt2 - add ground and a character that can move and jump
import random
import pygame
import gamebox
camera = gamebox.Camera(800,600)

character = gamebox.from_color(50, 50, "red", 15, 40)
character.yspeed = 0
walls = [gamebox.from_color(-100, 600, "black", 3000, 100), gamebox.from_color(450, 500, "black", 200, 15), gamebox.from_color(300, 400, "black", 200, 15), gamebox.from_color(450, 300, "black", 200, 15), gamebox.from_color(300, 200, "black", 200, 15), gamebox.from_color(450, 100, "black", 200, 15)]
coins = []
time = 9000
score = 0


def tick(keys):
    global time, score

    # clear display
    camera.clear("blue")

    # decrease timer per call of tick
    time -= 1

    # calculate timer
    seconds = str(int((time/ticks_per_second))).zfill(3)

    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 5
    character.yspeed += 1
    character.y = character.y + character.yspeed

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                 character.yspeed = -15
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    if time % 30 == 0:
        coin_x = random.randint(50, 750)
        coin_y = random.randint(400, 550)
        coins.append(gamebox.from_color(coin_x, coin_y, "yellow", 10, 10))

    for coin in coins:
        if character.touches(coin):
            score += 1
            coins.remove(coin)
        camera.draw(coin)


    # write timer and score to screen
    time_box = gamebox.from_text(650,30,"Time Remaining: " + seconds,"arial",24,"white")
    score_box = gamebox.from_text(75,30,"Score: " + str(score),"arial",24,"white")
    camera.draw(time_box)
    camera.draw(score_box)

    # draw the character
    camera.draw(character)

    # display the screen
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)