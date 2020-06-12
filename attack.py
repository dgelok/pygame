import pygame
import random
from classes import *
import math

pygame.font.init()
font = pygame.font.Font(None, 25)
win_message = font.render("Hit ENTER to play again!", True, (0, 0, 0))


KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275




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
    hero_image = pygame.image.load('images/link.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    stop_game = False

    monster = Monster(80, 300, width, height)
    monster2 = Monster(200, 20, width, height)
    hero = Hero(256, 240, width, height)
    direction = 2
    hspeed = 4
    won = False

    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1)

    while not stop_game:
        
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.speed_y = hspeed
                elif event.key == KEY_UP:
                    hero.speed_y = -hspeed
                elif event.key == KEY_LEFT:
                    hero.speed_x = -hspeed
                elif event.key == KEY_RIGHT:
                    hero.speed_x = hspeed
                elif event.key == pygame.K_RETURN:
                    if won == True:
                        monster.dead = False
                        won = False

            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = 0
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True
            
        
        # Game logic
        monster.update()
        hero.update()

        xs = abs(hero.x - monster.x)
        ys = abs(hero.y - monster.y)
        collide = math.sqrt(xs * xs + ys * ys)
        if collide < 32:
            if monster.dead == False:
                monster.dead = True
                pygame.mixer.music.load('sounds/win.wav')
                pygame.mixer.music.play()
                won = True
                
        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (hero.x, hero.y))
        if won:
            screen.blit(win_message, (150, 200))
        else:
            screen.blit(monster_image, (monster.x, monster.y))
        # screen.blit(monster_image, (monster2.x, monster2.y))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# if __name__ == '__main__':
#     main()

main()