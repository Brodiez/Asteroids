import pygame 
from player import *
from asteroid import *
from asteroidfield import *
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable , drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        updateable.update(dt)
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game Over!")
                return
            for shot in shots:
                if shot.check_collisions(asteroid):
                    shot.kill()
                    asteroid.kill()
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
