import pygame
from pygame.locals import *
import sys
import Background
 
pygame.init()
 
vec = pygame.math.Vector2 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
GRAV = 0.1
JUMP = -3

class Tank(pygame.sprite.Sprite):
    def __init__(self):
        self.all_sprites["bg"] = Background.background(WIDTH,HEIGHT)
        super().__init__() 
        self.FramePerSec = pygame.time.Clock()


        self.displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.FPS = 60
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0)
    
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_UP]:
            self.vel.y = JUMP
             
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        self.rect.midbottom = self.pos

    def gravity(self):
        if (pygame.Rect.colliderect(self.rect,  self.all_sprites["bg"].floor) == False):
            self.acc.y = GRAV
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc


