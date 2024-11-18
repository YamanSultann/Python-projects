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

screen = pygame.display.set_mode(screenwidth,screenheight)

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
num_of_enemies = 6

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
font = pygame.font.Font("freesansbold.tff",32)
textx = 10
texty = 10

over_font = pygame.font.Font("freesansbold.ttf",64)

def show_score():
    score = font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score(x,y))

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

def isCollision(enemyx,enemyy.bulletx,bullety):
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety) ** 2)
    return_distance < collision_distance