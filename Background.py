import pygame
class background(pygame.sprite.Sprite):
    def __init__(self,Width,Height):
        super().__init__()
        self.surf = pygame.Surface((Width, 20))
        self.surf.fill((255,0,0))
        self.floor = self.surf.get_rect(center = (Width/2, Height - 10))
        background_color = (255, 255, 255)
        screen = pygame.display.set_mode((Width, Height))
        screen.fill(background_color)