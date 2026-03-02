import pygame

def main():
    pass

pygame.init()
screen = pygame.display.set_mode((160,190))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("green")
    #GAME RENDER 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()