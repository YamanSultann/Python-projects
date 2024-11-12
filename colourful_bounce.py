import pygame
import random

pygame.init()

'blue' = pygame.color('blue')
'purple' = pygame.color('purple')
'pink' = pygame.color('pink')
'red' = pygame.color('red')

'yellow' = pygame.color('yellow')
'green' = pygame.color('green')
'orange' = pygame.color('orange')
'white' = pygame.color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super.__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_CHANGE_COLOUR_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

        def colour_change(self):
            self.image.fill(random.choice(['yellow','green','orange','white']))

        def background_colour_change():
            global bg_colour
            bg_colour = random.choice(['blue','purple','pink','red'])

        all_sprites_list = pygame.sprite.Group()
        sp1 = Sprite('white',20,30)
        sp1.rect.x = random.randint(0,480)
        sp1.rect.y = random.randint(0.370)
        all_sprites_list.add(sp1)

        screen = pygame.display.set_mode((500,400))
        pygame.display.set_caption("Boundary Sprite")
        bg_colour = 'blue'
        screen.fill = bg_colour

        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
                elif event.type == SPRITE_CHANGE_COLOUR_EVENT:
                    sp1.colour_change()
                
                elif event.type == BACKGROUND_COLOUR_CHANGE_EVENT:
                    background_colour_change()

            pygame.display.flip()