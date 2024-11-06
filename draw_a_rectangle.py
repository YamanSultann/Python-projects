import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(150,100,50,50))

    pygame.display.flip()