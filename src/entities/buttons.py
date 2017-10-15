import pygame as pg

from ..bootstrap import FONTS
from ..core.hud import BATTLE_SPRITES

FONT = pg.font.Font(FONTS['west-england.regular'], 20)

default_button = {
    'text_color': (255, 255, 255),
    'padding': 20,
    'color':  (0, 0, 0),
    'hover_color': (55, 55, 55),
    'disable': (100, 100, 100)
}

class Clickable(object):
    """docstring for Clickable"""

    def __init__(self):
        self.mouse_over = False

    def get_event(self, event):
        mouse_pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_pos):
                if(event.button == 1):
                    self.handle_click()
                if(event.button == 3):
                    self.handle_right_click()
        elif event.type == pg.MOUSEMOTION:
            mouse_over = self.rect.collidepoint(mouse_pos)
            if mouse_over != self.mouse_over:
                if mouse_over:
                    self.handle_mouse_enter()
                else:
                    self.handle_mouse_leave()
                self.mouse_over = mouse_over

    def handle_click(self):
        pass

    def handle_right_click(self):
        pass

    def handle_mouse_enter(self):
        pass

    def handle_mouse_leave(self):
        pass


class Button(pg.sprite.Sprite,  Clickable):
    """docstring for Button"""

    def __init__(self, text, color, pos, properties={}):
        super(Button, self).__init__()
        self.add(BATTLE_SPRITES)
        self.text = text
        self.color = color
        self._pos = pos
        self.properties = default_button.copy()
        self.properties.update(properties)
        self.mouse_over = False
        BATTLE_SPRITES.change_layer(self, 2)
        self.create()

    def create(self):
        self.label = FONT.render(
            self.text, False, self.properties['text_color'])
        self.label_rect = self.label.get_rect(topleft=self._pos)
        self.idle_image = pg.Surface((
            self.label_rect.width + self.properties['padding'] * 2,
            self.label_rect.height + self.properties['padding']
        ))
        self.idle_image.fill(self.properties['color'])
        self.hover_image = self.idle_image.copy()
        self.hover_image.fill(self.properties['hover_color'])
        self.image = self.idle_image
        self.rect = self.image.get_rect(topleft=self._pos)
        self.label_rect.x += self.properties['padding']
        self.label_rect.y += self.properties['padding'] // 2

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.label, self.label_rect)

    def handle_click(self):
        print("click")

    def handle_mouse_enter(self):
        self.image = self.hover_image

    def handle_mouse_leave(self):
        self.image = self.idle_image
