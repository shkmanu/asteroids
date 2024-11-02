from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, surface):
        pygame.draw.polygon(surface, (255, 255, 255), self.triangle(), 2)

    def rotate(self, multiplier):
        self.rotation += PLAYER_TURN_SPEED * multiplier

    def move(self, multiplier):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * multiplier

    def update(self, multiplier):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-multiplier)
        if keys[pygame.K_d]:
            self.rotate(multiplier)
        if keys[pygame.K_w]:
            self.move(multiplier)
        if keys[pygame.K_s]:
            self.move(0 - multiplier)


