import pygame
class background(pygame.sprite.Sprite):
    def __init__(self,Width,Height):
        super().__init__()
        self.surf = pygame.Surface((Width, 20))
        self.surf.fill((255,0,0))
        self.floor = self.surf.get_rect(center = (Width/2, Height - 70))
        background_color = (255, 255, 255)
        screen = pygame.display.set_mode((Width, Height))
        self.width = Width
        self.height= Height
        
        
        
        self.bg = pygame.image.load('tankBg.jpeg')
        self.bg_img = pygame.transform.scale(self.bg,(self.width,self.height))
    def draw(self):
        self.bg_img = pygame.transform.scale(self.bg,(self.width,self.height))
        return self.bg_img, (0,0)
        

            