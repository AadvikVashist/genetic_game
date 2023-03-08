import pygame
from pygame.locals import *
import sys
import Background
 
pygame.init()
 
vec = pygame.math.Vector2 
ACC = 0.5
FRIC = -0.12
GRAV = 0.1
JUMP = -2

class Tank(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__() 
        self.width = width
        self.height = height
        self.FramePerSec = pygame.time.Clock()
        self.index = 0

        self.displaysurface = pygame.display.set_mode((width, height))
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
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_UP] and (pygame.Rect.colliderect(self.rect, bg.floor) == True):
            self.vel.y = JUMP
             
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > self.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.width
            
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


