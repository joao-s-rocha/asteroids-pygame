import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    DIRECTIONS = ["up", "stoped", "down"]

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.random_direction_to_move = {
            "x_change": random.choice(self.DIRECTIONS), 
            "y_change": random.choice(self.DIRECTIONS)
        }

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            self.position, 
            self.radius, 
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += (self.velocity * dt)
