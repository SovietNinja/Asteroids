
import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)


    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            random_angle = random.uniform(20, 50)
            spawn_radius = self.radius - ASTEROID_MIN_RADIUS
            split1_dir = self.velocity.rotate(random_angle)
            split2_dir = self.velocity.rotate(-random_angle)
            split1 = Asteroid(self.position.x, self.position.y, spawn_radius)
            split2 = Asteroid(self.position.x, self.position.y, spawn_radius)
            split1.velocity = split1_dir * ASTEROID_SPLITS_SPEED
            split2.velocity = split2_dir * ASTEROID_SPLITS_SPEED


