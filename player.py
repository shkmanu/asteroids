from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shot_timer = 0

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

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity = shot.velocity * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

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
        if keys[pygame.K_SPACE]:
            if self.shot_timer > 0:
                self.shot_timer -= multiplier
            else:
                self.shoot()


