import pygame
from pygame.locals import *
import sys
import Tank
import Target
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
        a = Tank.Tank()
        b = Target.Target(WIDTH, HEIGHT)
        self.all_sprites["tank"] = a
        self.all_sprites["target"] = b
        self.all_sprites["bg"] = Background.background(WIDTH,HEIGHT)
        self.main()
    def intersects(self, rect: pygame.Rect) -> bool:
        if (self.ground.colliderect(rect) or
            self.left_wall.colliderect(rect) or
            self.right_wall.colliderect(rect) or
            self.top_wall.colliderect(rect)):
            return True
        elif (rect.x < 0 or rect.y < 0 or
                rect.x + rect.width > self.game_width or
                rect.y + rect.height > self.game_height):
            return True
        else:
            return False


    def intersects_goal(self, rect: pygame.Rect) -> bool:
        if (self.ground.colliderect(rect) or
            self.left_wall.colliderect(rect) or
            self.right_wall.colliderect(rect) or
            self.top_wall.colliderect(rect)):
            return True
        elif (rect.x < 0 or rect.y < 0 or
                rect.x + rect.width > self.game_width or
                rect.y + rect.height > self.game_height - 200):
            return True
        else:
            return False


    def ground_intersects(self, rect: pygame.Rect) -> bool:
        return (self.left_wall.colliderect(rect) or
                self.right_wall.colliderect(rect) or
                self.top_wall.colliderect(rect))


    def left_wall_intersects(self, rect: pygame.Rect) -> bool:
        return self.left_wall.colliderect(rect)


    def right_wall_intersects(self, rect: pygame.Rect) -> bool:
        return self.right_wall.colliderect(rect)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.displaysurface.fill((0,0,0))
        
            self.all_sprites["tank"].move(self.all_sprites["bg"])

            # if (pygame.Rect.colliderect(self.all_sprites["tank"].rect,  self.all_sprites["bg"].floor) == False):
            self.all_sprites["tank"].gravity(self.all_sprites["bg"])

            all_sprites_list = pygame.sprite.Group()
            all_sprites_list.add(self.all_sprites["tank"])
            all_sprites_list.add(self.all_sprites["target"])
            all_sprites_list.add(self.all_sprites["bg"])

            for entity in all_sprites_list:
                try:
                    self.displaysurface.blit(entity.surf, entity.floor)
                except:
                  self.displaysurface.blit(entity.surf, entity.rect)
 
            
            pygame.display.update()
            self.FramePerSec.tick(self.FPS)
if __name__ == '__main__':
    P1 = Player()