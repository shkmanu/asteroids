from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, multiplier):
        self.position += (multiplier * self.velocity)


