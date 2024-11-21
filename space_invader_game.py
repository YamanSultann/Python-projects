import pygame
import random
import math

screenwidth,screenheight = 800,500
player_start_x,player_start_y = 370,380
enemy_start_y_min,enemy_start_y_max = 50,150
enemy_speed_x,enemy_speed_y = 4,40
bullet_speed_y = 10
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screenwidth,screenheight))

background = pygame.image.load('background2.png')

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('player.png')
playerx = player_start_x
playery = player_start_y
playerx_change = 0

enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,screenwidth-64))
    enemyy.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)

bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = player_start_y
bulletx_change = 0
bullety_change = bullet_speed_y
bullet_state = "Ready"

score_value = 0
font = pygame.font.Font('FreeSansBold.ttf',32)
textx = 10
texty = 10

over_font = pygame.font.Font('FreeSansBold.ttf',64)

def show_score(x,y):
    score = font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg(x+16,y+16))

def isCollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety) ** 2)
    return distance < collision_distance

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerx_change = -5
            if event.key == pygame.K_d:
                playerx_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                fire_bullet(bulletx,bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_a,pygame.K_d]:
            playerx_change = 0

    playerx += playerx_change
    playerx = max(0,min(playerx,screenwidth-64))

    for i in range (num_of_enemies):
        if enemyy[i] > 340:
            for j in range (num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0 or enemyx[i] >= screenwidth - 64:
            enemyx_change[i] *= -1
            enemyy[i] += enemyy_change[i]

        if isCollision(enemyx[i],enemyy[i],bulletx,bullety):
            bullety = player_start_y
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0,screenwidth - 64)
            enemyy[i] = random.randint(enemy_start_y_min,enemy_start_y_max)
        enemy(enemyx[i],enemyy[i],i)

    if bullety <= 0:
        bullety = player_start_y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()