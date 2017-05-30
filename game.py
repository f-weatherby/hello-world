# Forrest Weatherby
# efw5xb

# efw5xb, dc5zd, aph8tb

import pygame
import gamebox
import math

def create_wall(x,y,length):
    new_wall = gamebox.from_color(x, y, "green", length, 20)
    walls.append(new_wall)

def create_coin(x,y):
    new_coin = gamebox.from_image(x,y, coin_sheet[0])
    new_coin.size = (28, 28)
    coins.append(new_coin)

def create_lava(x, y, length):
    pit = gamebox.from_color(x, y, "red", length, 10)
    lava.append(pit)


camera = gamebox.Camera(800, 600)
sheet=gamebox.load_sprite_sheet("https://s3-us-west-2.amazonaws.com/s.cdpn.io/160783/smurf_sprite.png", 4, 4)
sheet2=gamebox.load_sprite_sheet("https://s3-us-west-2.amazonaws.com/s.cdpn.io/160783/smurf_sprite.png", 4, 4)
frame = 0
frame2 = 0
player = gamebox.from_image(100, 70, sheet[frame])
player.size = 50, 50
player2 = gamebox.from_image(200, 70, sheet[frame])
player2.size = 50, 50
width = 10
walls = [gamebox.from_color(400, 595, "green", 1200, 20), gamebox.from_color(550, 500, "green", 600, 20), gamebox.from_color(0, 430, "green", 300, 20), gamebox.from_color(350,340,"green",300,20), gamebox.from_color(1230,430, "green", 520, 20)]
create_wall(1000, 230, 400)
create_wall(1100, 135, 10)
create_wall(1000, 130, 10)
create_wall(885, 80, 10)
create_wall(800, 100, 10)
create_wall(1850, 300, 700)
lava = [gamebox.from_color(550,495,"red",100,10),gamebox.from_color(0,425,"red",100,10)]
create_lava(950, 225, 300)
gameover_display = gamebox.from_text(camera.x,170, "GAME OVER", "Times New Roman", 72, "orange", bold=True)
score = 0
score2 = 0
counter = 0
time = 75
gameover = False
startscreen = True
right = True
#health = 5
quagmire_giggity = gamebox.from_image(1470, 390, "https://predaguy.files.wordpress.com/2011/05/glenn-quagmire.png")
quagmire_giggity.size = 50 ,50
enemy = True


# Coins:
coin_sheet = gamebox.load_sprite_sheet("https://www.acsu.buffalo.edu/~vewillia/final/coin.png",1,8)
coins = []
create_coin(550,400)
create_coin(800, 70)
create_coin(quagmire_giggity.x, quagmire_giggity.y - 50)
right = True
right2 = True
# Bullet list
bullets = []
# Background
oranges = gamebox.from_image(400, 300, "https://image.freepik.com/free-vector/abstract-background-with-a-geometric-design_1048-2803.jpg")
oranges.size = 800, 600
# Moving Block
moving_block = gamebox.from_color(1300, 200, "black", 50, 50)
down = True
# coordinates
coordinates_xpos = 0
# portal Trigger
portal_trigger = gamebox.from_color(800, 70, "black", 1, 1)
trigger_presence = True
# portal, center at 1100, 375
x1 = 1075
x2 = 1125
y1 = 350
y2 = 400
move_doors = False
portal_wait_counter = 0
#stairway
create_wall(1610, 240, 20)
create_wall(1750, 210, 20)
create_wall(1850, 200, 20)
create_wall(1970, 178, 20)
create_wall(1996, 114, 20)
create_coin(1994, 72)
#stairway enemy
stairway_enemy = gamebox.from_color(2167, 265, "black", 40, 40)
sdown = True
s_enemy_presence = False
pellets = []
# Health Meter
health_meter = [gamebox.from_color(360, 30, "pink", 60, 30),
                gamebox.from_color(420, 30, "pink", 60, 30),
                gamebox.from_color(480, 30, "pink", 60, 30),
                gamebox.from_color(530, 30, "pink", 60, 30),
                gamebox.from_color(580, 30, "pink", 60, 30)]

# two players
two_players = False
# health meter 2
health_meter2 = [gamebox.from_color(360, 64, "pink", 60, 30),
                gamebox.from_color(420, 64, "pink", 60, 30),
                gamebox.from_color(480, 64, "pink", 60, 30),
                gamebox.from_color(530, 64, "pink", 60, 30),
                gamebox.from_color(580, 64, "pink", 60, 30)]


def tick(keys):
    global score, gameover, counter, frame, right, time, health, startscreen, enemy,\
        down,coordinates_xpos,trigger_presence,x1,x2,y1,y2,move_doors,portal_wait_counter,\
        sdown,s_enemy_presence,two_players,right2,frame2,score2

    if startscreen == True:
        camera.clear("deepskyblue")

        textline1 = gamebox.from_text(camera.x, 50, "Smurfs", "Times New Roman", 70, "white", bold=True)
        textline2 = gamebox.from_text(camera.x, 100, "Forrest Weatherby: efw5xb", "Times New Roman", 25, "lavender", bold=True)
        textline3 = gamebox.from_text(camera.x, 125, "Phillip Head: aph8tb", "Times New Roman", 25, "lavender", bold=True)
        textline4 = gamebox.from_text(camera.x, 150, "Diva Chowdhary: dc5zd", "Times New Roman", 25, "lavender", bold=True)
        textline5 = gamebox.from_text(camera.x, 200, "Help the ~Smurf~ collect all the coins by ",
                                      "Times New Roman", 30, "bisque", bold=True)
        textline6 = gamebox.from_text(camera.x, 225, "moving the left and right arrow keys. ",
                                      "Times New Roman", 30, "bisque", bold=True)
        textline7 = gamebox.from_text(camera.x, 250, "Avoid the enemies and red lava by jumping ",
                                      "Times New Roman", 30, "bisque", bold=True)
        textline8 = gamebox.from_text(camera.x, 275, "by pressing the up arrow key.",
                                      "Times New Roman", 30, "bisque", bold=True)
        textline9 = gamebox.from_text(camera.x, 325, "Press the SPACE bar to begin the game. ",
                                      "Times New Roman", 30, "linen", bold=True)
        textline10 = gamebox.from_text(camera.x, 375, "~Good Luck!~",
                                      "Times New Roman", 30, "linen", bold=True)
        textline11 = gamebox.from_text(camera.x, 450, "Click here for two player (W = up, A = left, D = right)", "Times New Roman", 20, "black", bold=True)
        button = gamebox.from_color(camera.x, 450, "red", 650, 30)



        camera.draw(textline1)
        camera.draw(textline2)
        camera.draw(textline3)
        camera.draw(textline4)
        camera.draw(textline5)
        camera.draw(textline6)
        camera.draw(textline7)
        camera.draw(textline8)
        camera.draw(textline9)
        camera.draw(textline10)
        camera.draw(button)
        camera.draw(textline11)

        camera.display()
        if 75 < camera.mouse[0] < 725:
            if 435 < camera.mouse[1] < 465:
                if camera.mouseclick:
                    two_players = True
                    startscreen = False
        if pygame.K_SPACE in keys:
            startscreen = False



    if startscreen == False:
        if two_players:
            camera.clear("cyan")
            camera.draw(oranges)
            counter += 1

            # Scoreboard 1
            score_banner1 = gamebox.from_text(camera.x - 300, camera.y - 270, "Score: " + str(score), "Times New Roman", 32,"gold")
            score_banner1.left = camera.x - 380
            health_banner1 = gamebox.from_text(camera.x - 50, 30, "Player 1 Health:", "Times New Roman", 22, "pink")
            health_banner1.left = camera.x - 250

            # Scoreboard 2
            score_banner2 = gamebox.from_text(camera.x - 300, camera.y - 250, "Score: " + str(score2), "Times New Roman", 32,"gold")
            score_banner2.left = camera.x - 380
            health_banner2 = gamebox.from_text(camera.x - 50, 70, "Player 2 Health:", "Times New Roman", 22, "pink")
            health_banner2.left = camera.x - 250


            # player 2
            if pygame.K_d in keys:
                if not right2:
                    player2.flip()
                player2.x += 5
                frame2 += 1
                player2.image = sheet2[frame2]
                if frame2 == 15:
                    frame2 = 0
                right2 = True
            if pygame.K_a in keys:
                if right2:
                    player2.flip()
                player2.x -= 5
                frame2 += 1
                player2.image = sheet2[frame2]
                if frame2 == 15:
                    frame2 = 0
                right2 = False
            if pygame.K_s in keys:
                player2.y += 5
            if pygame.K_q in keys:
                gamebox.stop_loop()

            # Gravity
            player.speedy += .5
            player.move_speed()
            player2.speedy += .5
            player2.move_speed()

            # Screen moves with player
            if player.x > camera.x + 300 or player2.x > camera.x + 300:
                camera.x += 400
                oranges.x += 400
                coordinates_xpos += 400
                for i in health_meter:
                    i.x += 400
                for i in health_meter2:
                    i.x += 400
            if player.x < camera.x - 300 or player2.x < camera.x - 300:
                camera.x -= 400
                oranges.x -= 400
                for i in health_meter:
                    i.x -= 400
                for i in health_meter2:
                    i.x -= 400
                coordinates_xpos -= 400

            # Lava logic
            for pool in lava:
                if two_players:
                    if player.touches(pool, -30, 0):
                        camera.draw(gamebox.from_text(camera.x,170, "GAME OVER! Player 2 Wins!", "Times New Roman", 50, "orange", bold=True))
                        gamebox.pause()
                    elif player2.touches(pool, -30, 0):
                        camera.draw(gamebox.from_text(camera.x,170, "GAME OVER! Player 1 Wins!", "Times New Roman", 50, "orange", bold=True))
                        gamebox.pause()

            # Walls logic
            for wall in walls:
                camera.draw(wall)
                if player.touches(wall):
                    player.move_to_stop_overlapping(wall)
                if player2.touches(wall):
                    player2.move_to_stop_overlapping(wall)
                if player.bottom_touches(wall):
                    if pygame.K_UP in keys:
                        player.yspeed -= 10
                if player2.bottom_touches(wall):
                    if pygame.K_w in keys:
                        player2.yspeed -= 10
            # Player controls
            if pygame.K_RIGHT in keys:
                if not right:
                    player.flip()
                player.x += 5
                frame += 1
                player.image = sheet[frame]
                if frame == 15:
                    frame = 0
                right = True
            if pygame.K_LEFT in keys:
                if right:
                    player.flip()
                player.x -= 5
                frame += 1
                player.image = sheet[frame]
                if frame == 15:
                    frame = 0
                right = False
            if pygame.K_DOWN in keys:
                player.y += 5
            if pygame.K_q in keys:
                gamebox.stop_loop()


            # Coins
            for coin in coins:
                if player.touches(coin, 0, 0):
                    coins.remove(coin)
                    score += 10
                elif player2.touches(coin, 0, 0):
                    coins.remove(coin)
                    score2 += 10
                else:
                    coin_index = int(counter/3) % 8
                    coin.image = coin_sheet[coin_index]
            # Moving Block
            if down:
                moving_block.y += 1
            else:
                moving_block.y -= 1
            if moving_block.y == 400:
                down = False
            elif moving_block.y == 200:
                down = True
            if player.touches(moving_block):
                player.move_to_stop_overlapping(moving_block)
            if player2.touches(moving_block):
                player2.move_to_stop_overlapping(moving_block)
            if player.bottom_touches(moving_block):
                if pygame.K_UP in keys:
                    player.yspeed -= 10
            if player2.bottom_touches(moving_block):
                if pygame.K_w in keys:
                    player2.yspeed -= 10

            # Stairway enemy
            if player.contains(1100, 390) and not trigger_presence:
                s_enemy_presence = True
            if player2.contains(1100, 390) and not trigger_presence:
                s_enemy_presence = True
            if sdown and s_enemy_presence:
                stairway_enemy.y -= 0.5
            else:
                stairway_enemy.y += 0
            if stairway_enemy.y == 40:
                sdown = False
            if s_enemy_presence:
                camera.draw(stairway_enemy)
                if counter % 10 == 0:
                    pellets.append(gamebox.from_color(stairway_enemy.x, stairway_enemy.y, "white", 5, 5))
                for pellet in pellets:
                    pellet.x -= 4
                    if pellet.x < 1500:
                        pellets.remove(pellet)
                    camera.draw(pellet)
                    if player.touches(pellet, -10, 0):
                        pellets.remove(pellet)
                        health_meter.remove(health_meter[len(health_meter)-1])
                    if player2.touches(pellet, -10, 0):
                        pellets.remove(pellet)
                        health_meter2.remove(health_meter2[len(health_meter2)-1])
            if player.bottom_touches(stairway_enemy):
                s_enemy_presence = False
            if player2.bottom_touches(stairway_enemy):
                s_enemy_presence = False

            # Bullets
            if enemy == True:
                if gameover == False:
                    if counter % 40 == 0:
                        bullets.append(
                            gamebox.from_color(quagmire_giggity.x, quagmire_giggity.y + 15, "yellow", 5, 5))
                for bullet in bullets:
                    bullet.x -= 3
                    if bullet.x < 980:
                        bullets.remove(bullet)
                    camera.draw(bullet)
                    if player.touches(bullet, -10, 0):
                        bullets.remove(bullet)
                        health_meter.remove(health_meter[len(health_meter)-1])
                    if player2.touches(bullet, -10, 0):
                        bullets.remove(bullet)
                        health_meter2.remove(health_meter2[len(health_meter2)-1])
                if player.bottom_touches(quagmire_giggity):
                    enemy = False

            # Portal trigger
            if player.touches(portal_trigger):
                trigger_presence = False
            if trigger_presence:
                camera.draw(portal_trigger)

            # Portal
            if not trigger_presence:
                portal_wait_counter += 1
                camera.draw(gamebox.from_color(1100, 375, "black", 100, 100))
                portal_doors = [gamebox.from_color(x1, y1, "blue", 50, 50),
                                gamebox.from_color(x2, y1, "orange", 50, 50),
                                gamebox.from_color(x1, y2, "orange", 50, 50),
                                gamebox.from_color(x2, y2, "blue", 50, 50)]
                if portal_wait_counter == 70:
                    move_doors = True
                if x1 == 1025:
                    move_doors = False
                if move_doors:
                    x1 -= 1
                    x2 += 1
                    y1 -= 1
                    y2 += 1
                for door in portal_doors:
                    camera.draw(door)
                if player.contains(1100, 390):
                    trigger_presence = True
                    player.center = [1520, 250]
            # Drawing functions
            for pool in lava:
                camera.draw(pool)
            for coin in coins:
                camera.draw(coin)
            camera.draw(player)
            camera.draw(player2)
            camera.draw(score_banner1)
            camera.draw(health_banner1)
            camera.draw(score_banner2)
            camera.draw(health_banner2)
            if len(health_meter) > 0:
                for i in health_meter:
                    camera.draw(i)
            if len(health_meter2) > 0:
                for k in health_meter2:
                    camera.draw(k)
            if enemy == True:
                camera.draw(quagmire_giggity)
            camera.draw(moving_block)

            # Gameover
            if player.y > 650 or len(health_meter) < 1:
                camera.draw(gamebox.from_text(camera.x,170, "GAME OVER! Player 2 Wins!", "Times New Roman", 50, "orange", bold=True))
                gamebox.pause()
            if player2.y > 650 or len(health_meter2) < 1:
                camera.draw(gamebox.from_text(camera.x,170, "GAME OVER! Player 1 Wins!", "Times New Roman", 50, "orange", bold=True))
                gamebox.pause()

            if gameover:
                gameover_display.center = [camera.x, 170]
                camera.draw(gameover_display)
                gamebox.pause()

            time += 1
            seconds = str(int((time / (ticks_per_second/1.4)))).zfill(3)
            time_box = gamebox.from_text(camera.x + 300, 30, "Time: " + seconds, "arial", 24, "white")
            camera.draw(time_box)
        else:
            camera.clear("cyan")
            camera.draw(oranges)
            counter += 1

            score_banner = gamebox.from_text(camera.x - 300, camera.y - 270, "Score: " + str(score), "Times New Roman",
                                             32, "gold")
            score_banner.left = camera.x - 380
            health_banner = gamebox.from_text(camera.x - 50, 30, "Health:", "Times New Roman", 32, "pink")
            health_banner.left = camera.x - 180

            # Gravity
            player.speedy += .5
            player.move_speed()

            # Screen moves with player
            if player.x > camera.x + 400:
                camera.x += 700
                oranges.x += 700
                coordinates_xpos += 700
                for i in health_meter:
                    i.x += 700
            elif player.x < camera.x - 400:
                camera.x -= 700
                oranges.x -= 700
                for i in health_meter:
                    i.x -= 700
                coordinates_xpos -= 700

            # Lava logic
            for pool in lava:
                if player.touches(pool, -30, 0):
                    gameover = True

            # Walls logic
            for wall in walls:
                camera.draw(wall)
                if player.touches(wall):
                    player.move_to_stop_overlapping(wall)
                if player.bottom_touches(wall):
                    if pygame.K_UP in keys:
                        player.yspeed -= 10
            # Player controls
            if pygame.K_RIGHT in keys:
                if not right:
                    player.flip()
                player.x += 5
                frame += 1
                player.image = sheet[frame]
                if frame == 15:
                    frame = 0
                right = True
            if pygame.K_LEFT in keys:
                if right:
                    player.flip()
                player.x -= 5
                frame += 1
                player.image = sheet[frame]
                if frame == 15:
                    frame = 0
                right = False
            if pygame.K_DOWN in keys:
                player.y += 5
            if pygame.K_q in keys:
                gamebox.stop_loop()

            # Coins
            for coin in coins:
                if player.touches(coin, 0, 0):
                    coins.remove(coin)
                    score += 10
                else:
                    coin_index = int(counter / 3) % 8
                    coin.image = coin_sheet[coin_index]
            # Moving Block
            if down:
                moving_block.y += 1
            else:
                moving_block.y -= 1
            if moving_block.y == 400:
                down = False
            elif moving_block.y == 200:
                down = True
            if player.touches(moving_block):
                player.move_to_stop_overlapping(moving_block)
            if player.bottom_touches(moving_block):
                if pygame.K_UP in keys:
                    player.yspeed -= 10

            # Stairway enemy
            if player.contains(1100, 390) and not trigger_presence:
                s_enemy_presence = True
            if sdown and s_enemy_presence:
                stairway_enemy.y -= 0.5
            else:
                stairway_enemy.y += 0
            if stairway_enemy.y == 40:
                sdown = False
            if s_enemy_presence:
                camera.draw(stairway_enemy)
                if counter % 10 == 0:
                    pellets.append(gamebox.from_color(stairway_enemy.x, stairway_enemy.y, "white", 5, 5))
                for pellet in pellets:
                    pellet.x -= 4
                    if pellet.x < 1500:
                        pellets.remove(pellet)
                    camera.draw(pellet)
                    if player.touches(pellet, -10, 0):
                        pellets.remove(pellet)
                        health_meter.remove(health_meter[len(health_meter) - 1])
            if player.bottom_touches(stairway_enemy) or player2.bottom_touches(stairway_enemy):
                s_enemy_presence = False

            # Bullets
            if enemy == True:
                if gameover == False:
                    if counter % 40 == 0:
                        bullets.append(
                            gamebox.from_color(quagmire_giggity.x, quagmire_giggity.y + 15, "yellow", 5, 5))
                for bullet in bullets:
                    bullet.x -= 3
                    if bullet.x < 980:
                        bullets.remove(bullet)
                    camera.draw(bullet)
                    if player.touches(bullet, -10, 0):
                        bullets.remove(bullet)
                        health_meter.remove(health_meter[len(health_meter) - 1])
                if player.bottom_touches(quagmire_giggity) or player2.bottom_touches(quagmire_giggity):
                    enemy = False

            # Portal trigger
            if player.touches(portal_trigger):
                trigger_presence = False
            if trigger_presence:
                camera.draw(portal_trigger)

            # Portal
            if not trigger_presence:
                portal_wait_counter += 1
                camera.draw(gamebox.from_color(1100, 375, "black", 100, 100))
                portal_doors = [gamebox.from_color(x1, y1, "blue", 50, 50),
                                gamebox.from_color(x2, y1, "orange", 50, 50),
                                gamebox.from_color(x1, y2, "orange", 50, 50),
                                gamebox.from_color(x2, y2, "blue", 50, 50)]
                if portal_wait_counter == 70:
                    move_doors = True
                if x1 == 1025:
                    move_doors = False
                if move_doors:
                    x1 -= 1
                    x2 += 1
                    y1 -= 1
                    y2 += 1
                for door in portal_doors:
                    camera.draw(door)
                if player.contains(1100, 390):
                    trigger_presence = True
                    player.center = [1520, 250]
            # Drawing functions
            for pool in lava:
                camera.draw(pool)
            for coin in coins:
                camera.draw(coin)
            camera.draw(player)
            camera.draw(score_banner)
            camera.draw(health_banner)
            if len(health_meter) > 0:
                for i in health_meter:
                    camera.draw(i)
            if enemy == True:
                camera.draw(quagmire_giggity)
            camera.draw(moving_block)

            # Gameover
            if player.y > 650 or len(health_meter) < 1:
                gameover = True

            if gameover:
                gameover_display.center = [camera.x, 170]
                camera.draw(gameover_display)
                gamebox.pause()

            time += 1
            seconds = str(int((time / (ticks_per_second / 1.4)))).zfill(3)
            time_box = gamebox.from_text(camera.x + 300, 30, "Time: " + seconds, "arial", 24, "white")
            camera.draw(time_box)


        camera.display()

ticks_per_second = 70
gamebox.timer_loop(ticks_per_second, tick)