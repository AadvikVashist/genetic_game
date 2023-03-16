
import pygame
from pygame.locals import *
import math
vec = pygame.math.Vector2 
CC = 0.5
GRAV = 0.4
JUMP = -2
import time
class projectile(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__() 
        self.projectile_list = []
        self.acc = vec(0,GRAV)
        self.width = width
        self.height = height
        self.time_since_last = time.time()

    def new_bullet(self, velocity, direction, color, pos,radius):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE] and time.time() - self.time_since_last > 0.2:
            self.time_since_last = time.time()
            pos.y-=15
            vel = [velocity*math.cos(math.radians(direction)),-velocity*math.sin(math.radians(direction))]
            self.projectile_list.append({"color" : color, "pos" : vec(pos), "vel" : vec(vel), "radius" : radius, "acc" : vec(0,GRAV)})
    def draw(self,win):
        chars = []
        for i in self.projectile_list: #0 is x and y is 1  2 is radius 
            chars.append(pygame.draw.circle(win, i["color"], i["pos"], i["radius"]))
        return chars
    def move(self, bg):
        index = 0
        while index < len(self.projectile_list):
            if self.projectile_list[index]["pos"].y < bg.floor.top:
                self.projectile_list[index]["acc"] =  vec(0,GRAV)
                self.projectile_list[index]["vel"] += self.projectile_list[index]["acc"]
                self.projectile_list[index]["pos"] += self.projectile_list[index]["vel"] + 0.5 * self.acc
                if self.projectile_list[index]["pos"].x > self.width or self.projectile_list[index]["pos"].x < 0:
                    del self.projectile_list[index]
                else:
                    index+=1         
            else:
                self.projectile_list[index]["acc"] =  vec(0,0)
                del self.projectile_list[index]
       
        # self.win_animation( bg)
