from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, multiplier):
        self.position += (multiplier * self.velocity)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        else:
            random_angle = random.uniform(20, 50)
            split1_velocity = self.velocity.rotate(random_angle)
            split2_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split1_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            split2_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            split1_asteroid.velocity = split1_velocity * 1.2
            split2_asteroid.velocity = split2_velocity * 1.2





