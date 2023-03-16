import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import RectType
from enum import Enum
import Game

BG_COLOR = (106, 159, 181)
TXT_COLOR = (255, 255, 255)

def create_surface(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold = True)
    surface, _ = font.render(text = text, fgcolor = text_rgb, bgcolor = bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        self.mouse_over = False

        default_image = create_surface(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        super().__init__()

        self.action = action

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]
    
    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    game_state = 0

    while True: 
        if game_state == 0:
            game_state = title_screen(screen)

        if game_state == 1:
            game_state = play(screen)

        if game_state == -1:
            pygame.quit()
            return

def title_screen(screen):
    button_quit = UIElement(center_position=(500, 400),font_size=30,bg_rgb=BG_COLOR,text_rgb=TXT_COLOR,text="QUIT",action = -1)
    button_start = UIElement(center_position=(300, 400),font_size=30,bg_rgb=BG_COLOR,text_rgb=TXT_COLOR,text="START",action = 1)

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BG_COLOR)

        ui_action = button_quit.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        button_quit.draw(screen)

        ui_action1 = button_start.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action1 is not None:
            return ui_action1
        button_start.draw(screen)
        
        pygame.display.flip()

def play(screen):
    P1 = Game.Player()

if __name__ == "__main__":
    main()