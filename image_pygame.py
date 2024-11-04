import pygame

pygame.init()
screenwidth, screenheight = 500, 500

display_surface = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('Addidng image an dbackground image')

background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (screenwidth, screenheight))

penguin_image = pygame.transform.scale(
    pygame.image.load('weird.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(screenwidth // 2,
                                              screenheight // 2 - 30))

text = pygame.font.Font(None,36).render('Hello world', True,
                                        pygame.Color('black'))
text_rect = text.get_rect(center=(screenwidth // 2,
                                  screenheight // 2 + 100))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text,text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()