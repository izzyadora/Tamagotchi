import pygame
import config
from view.pet_view import PetView

def config_pygame():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #UPDATE
        PetView.update(dt)
        #DRAW
        screen.fill("green")
        PetView.draw(screen)

        pygame.display.flip()

    pygame.quit()

def main():
    config_pygame()


main()