import pygame
import random
from classes import *



def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    stop_game = False

    monster = Monster(80, 300, 1, 0, 512, 480)
    direction = 2

    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True
        
        # Game logic
        monster.move()

        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (256, 240))
        screen.blit(monster_image, (monster.x, monster.y))
        pygame.display.update()
        clock.tick(60)

        

    pygame.quit()

# if __name__ == '__main__':
#     main()

main()