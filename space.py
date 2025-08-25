''' space war  type game '''

import sys
import pygame
from game import Game


# CONSTANTS
SCREEN_WIDTH = 750      # window width
SCREEN_HEIGTH = 700     # window height
FPS = 60                # frames per second for clock
GREY = (29, 29, 27)     # dark gey color for background


def main():

    #Initialize Pygame
    pygame.init()

    # Creat the display surface (window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

    # Set the window title
    pygame.display.set_caption("Space Wars")

    # set game clock
    clock = pygame.time.Clock()

    # set game screen dimensions
    game = Game(SCREEN_WIDTH, SCREEN_HEIGTH)

    # Game Loop
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # updating
        game.spaceship_group.update()

        # draw screen with backgroud color
        screen.fill(GREY)
        game.spaceship_group.draw(screen)
        game.spaceship_group.sprite.lasers_group.draw(screen)
        for obstacle in game.obstacles:
            obstacle.blocks_group.draw(screen)

        # update game screen
        pygame.display.update()

        # loop runs n frames per second
        clock.tick(FPS)
 

if __name__ == "__main__":
    main()