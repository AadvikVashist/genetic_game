import random
import pygame
from pygame.locals import *
vec = pygame.math.Vector2 
ACC = 0.5
FRIC = 0.92
GRAV = 0.1

class Target(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__() 
        self.width = width
        self.height = height
        self.FramePerSec = pygame.time.Clock()
        self.index = 0
        self.displaysurface = pygame.display.set_mode((width, height))
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((0,100,100))
        self.rect = self.surf.get_rect()
        self.FPS = 60
        self.pos = vec((10, 50))
        self.vel = vec(0,0)
        self.acc = vec(0.5,0)

    def move(self, bg):
        self.vel += self.acc
        self.vel*=FRIC
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > self.width:
            self.pos.x = self.width
            self.acc = vec(-0.4,0)
        if self.pos.x < 0:
            self.pos.x = 0
            self.acc = vec(0.4,0)
            
        self.rect.midbottom = self.pos
        # self.win_animation( bg)
    def gravity(self, bg):
        if (pygame.Rect.colliderect(self.rect, bg.floor) == False):
            self.acc.y = GRAV
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
        else:
            self.pos.y = bg.floor.y
