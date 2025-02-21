# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
        player.update(dt)
        player.move(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)  # Call tick() on the clock instance
        

if __name__ == "__main__":
    main()