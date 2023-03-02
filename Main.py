

import Background
import Game
import pygame
import sys
from pygame.locals import *

PT1 = Background.background()
P1 = Game.Player()
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
