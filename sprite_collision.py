import pygame
import random

screenwidth,screenheight = 500,400
movement_speed = 5
font_size = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("background.png"),screenwidth,screenheight)

font = pygame.font.SysFont("Times New Roman",font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color('black'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

    def move(self,x_change,y_change):
        self.rect.x = max(min(self.rect.x + x_change,screenwidth = self.rect.width),0)
        self.rect.y = max(min(self.rec.y + y_change,screenheight = self.rect.width),0)

screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('white'),20,20)
sprite1.rect.x,sprite1.rect.y = random.randint(0,screenwidth-sprite1.rect.width),random.randint(0,screenheight-sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('white'),20,20)
sprite2.rect.x,sprite2.rect.y = random.randint(0,screenwidth-sprite2.rect.width),random.randint(0,screenheight-sprite2.rect.height)
all_sprites.add(sprite2)

running,won = True,False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
        
    if not won:
        keys = pygame.key.get_pressed()
        x_change = ([pygame.K_d] - keys[pygame.K_a])
        y_change = ([pygame.K_s] - keys[pygame.K_w])
        sprite1.move(x_change,y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image,(0,0))
    all_sprites.draw(screen)

    if won:
        win_text