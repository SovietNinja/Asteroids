# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *

drawable = pygame.sprite.Group()
updatable = pygame.sprite.Group()
Player.containers = (updatable, drawable) 

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
       #player.update(dt)
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        #player.draw(screen)
        dt = (clock.tick(60))/1000
        pygame.display.flip()


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
    
