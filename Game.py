import pygame
from pygame.locals import *
import sys
import Tank
import Target
import Projectile
vec = pygame.math.Vector2 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12

import Background

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__() 
        pygame.init()
        self.FramePerSec = pygame.time.Clock()

        self.displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game")
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.FPS = 60
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
        self.all_sprites ={}
        a = Tank.Tank(WIDTH,HEIGHT)
        b = Target.Target(WIDTH, HEIGHT)
        c = Projectile.projectile(WIDTH,HEIGHT)
        self.all_sprites["tank"] = a
        self.all_sprites["target"] = b
        self.all_sprites["projectile"] = c
        self.all_sprites["bg"] = Background.background(WIDTH,HEIGHT)
        self.main()
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.displaysurface.fill((0,0,0))
        
            self.all_sprites["tank"].move(self.all_sprites["bg"])
            self.all_sprites["target"].move(self.all_sprites["bg"])
            self.all_sprites["bg"].draw()
            self.all_sprites["projectile"].move(self.all_sprites["bg"])
            self.all_sprites["projectile"].new_bullet(15,60,(255,255,255),self.all_sprites["tank"].pos,10)
            # if (pygame.Rect.colliderect(self.all_sprites["tank"].rect,  self.all_sprites["bg"].floor) == False):
            self.all_sprites["tank"].gravity(self.all_sprites["bg"])

            all_sprites_list = pygame.sprite.Group()
            all_sprites_list.add(self.all_sprites["bg"])
            all_sprites_list.add(self.all_sprites["tank"])
            all_sprites_list.add(self.all_sprites["target"])
            all_sprites_list.add(self.all_sprites["projectile"])

            for entity in all_sprites_list:
                try:
                    self.displaysurface.blit(entity.surf, entity.floor)
                except:
                    try:    
                        self.displaysurface.blit(entity.surf, entity.rect)
                    except:
                        pass
                try:
                    self.displaysurface.blit(entity.bg_img, (0,0))
                except:
                    pass
            self.all_sprites["projectile"].draw(self.displaysurface)

            pygame.display.update()
            self.FramePerSec.tick(self.FPS)
Player()