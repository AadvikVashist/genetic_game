import pygame
from pygame.locals import *
import sys
import Background
import math
 
pygame.init()
 
vec = pygame.math.Vector2 
ACC = 0.5
FRIC = -0.12
GRAV = 0.1
JUMP = -2
WIDTH = 1
HEIGHT = 1
POWER = 5
ANGLE = -45

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.width = WIDTH
        self.height = HEIGHT
        self.FramePerSec = pygame.time.Clock()
        self.index = 0

        self.displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.FPS = 60
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self, bg):
        self.acc = vec(0,0)
    
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_SPACE]:
            self.pos.x = 0
            self.pos.y = 500
            self.vel.x = POWER*math.cos(ANGLE)
            self.vel.y = POWER*math.sin(ANGLE)
             

        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
         
            
        self.rect.midbottom = self.pos
        # self.win_animation( bg)
    def gravity(self, bg):
        if (pygame.Rect.colliderect(self.rect, bg.floor) == False):
            self.acc.y = GRAV
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
        else:
            self.pos.y = bg.floor.y
    
    def win_animation(self, bg):
        self.index+=1
        if (pygame.Rect.colliderect(self.rect, bg.floor) == False):
            self.acc.y = GRAV
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
        else:
            self.pos.y = bg.floor.y
            JUMP = -1
            self.vel.y = JUMP


