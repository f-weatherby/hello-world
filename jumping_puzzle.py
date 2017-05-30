# Forrest Weatherby
# efw5xb

# jumping puzzle game - pt1 - draw the score and timer on the screen

import pygame
import gamebox
camera = gamebox.Camera(800,600)

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
    #zfill makes it 060 vs 60.

    # write timer and score to screen
    time_box = gamebox.from_text(650,30,"Time Remaining: " + seconds,"arial",24,"white")
    score_box = gamebox.from_text(75,30,"Score: " + str(score),"arial",24,"white")
    camera.draw(time_box)
    camera.draw(score_box)
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)