from circleshape import *


SHOT_RADIUS = 5

class Shot(CircleShape):

    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position ,SHOT_RADIUS)
    def update(self, dt):        
        self.position += (self.velocity * dt)
