import random
import pygame as pg

from ..bootstrap import GFX, FONTS
from .buttons import Button, Clickable

CARD_SIZE = (128, 176)

FONT = pg.font.Font(FONTS['west-england.regular'], 20)


class Card(pg.sprite.Sprite, Clickable):
    """docstring for Card"""

    def __init__(self, pos):
        super(Card, self).__init__()
        self.face_up = GFX['testcard']
        self.face_down = pg.Surface(CARD_SIZE)
        self.face_down.fill((100, 100, 100))
        self.rect = self.face_up.get_rect(topleft=pos)
        self.mask_rect = self.rect.copy()
        self.mask_rect.topleft = 0, 0
        self.flip_factor = -1
        self.faceing_up = True
        self.pos = pos
        self.fliping = False
        self.flip_speed = 4
        self.bounce_speed = 1

        self.message = Button("Hello", (233, 45, 132), (self.rect.right + 10, self.rect.top))
        self.mouse_over = False

    def get_event(self, event):
        super(Card, self).get_event(event)
        self.message.get_event(event)

    def handle_click(self):
        if self.fliping:
            return
        self.fliping = True

    # def is_mouse_hover(self, mouse_pos):
    #     return mouse_pos[0] >= self.rect.x and \
    #             mouse_pos[0] <= self.rect.x + self.rect.width and \
    #             mouse_pos[1] >= self.rect.top and \
    #             mouse_pos[1] <= self.rect.top + self.rect.height

    def rotate(self):
        self.face_up = pg.transform.rotate(self.face_up, 90)
        self.mask_rect = self.face_up.get_rect()

    def update(self):
        if self.fliping:
            self.mask_rect.width += self.flip_speed * self.flip_factor
            x = self.pos[0] + (self.rect.width - self.mask_rect.width) // 2
            self.rect.x = x
            self.rect.y -= self.bounce_speed * self.flip_factor
            if self.mask_rect.width == 0:
                self.flip_factor *= -1
                self.faceing_up = not self.faceing_up
            if self.mask_rect.width == self.rect.width:
                self.fliping = False
                self.flip_factor *= -1

    def draw(self, surface):
        if(self.faceing_up):
            surface.blit(self.face_up, self.rect, self.mask_rect)
        else:
            surface.blit(self.face_down, self.rect, self.mask_rect)
        self.message.draw(surface)
        # surface.blit(self.image, self.rect)
