import random
import pygame
class Target(pygame.sprite.Sprite):
    def __init__(self,width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.width + 20, self.width + 100),
                random.randint(0, self.height),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()