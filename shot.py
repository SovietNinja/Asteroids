import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_TURN_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
    
    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt

   # def rotate(self, dt):
    #    self.rotation += PLAYER_TURN_SPEED * dt


