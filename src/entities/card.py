import random
import pygame as pg

from ..bootstrap import GFX, FONTS
from .buttons import Button, Clickable
from ..core.hud import BATTLE_SPRITES

CARD_SIZE = (128, 176)

FONT = pg.font.Font(FONTS['west-england.regular'], 40)


CARD_TYPE = ['GRASS', 'FIRE', 'WATER', 'NORMAL']
TYPE_COLORS = {
    'GRASS': (113, 185, 81),
    'FIRE': (225, 119, 51),
    'WATER': (103, 129, 179),
    'NORMAL': (156, 160, 113)
}
CARD_RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


def load_cardset():
    x, y = 0, 0
    for card_type in CARD_TYPE:
        GFX[card_type] = {}
        for rank in CARD_RANKS:
            GFX[card_type][rank] = GFX['cardset'].subsurface(
                0, y, CARD_SIZE[0], CARD_SIZE[1]).copy()
            r = FONT.render(str(rank), True, TYPE_COLORS[card_type])
            GFX[card_type][rank].blit(r, (8, 8))
            r = pg.transform.rotate(r, 180)
            rect = r.get_rect()
            rect.bottom = 168
            rect.right = 120
            GFX[card_type][rank].blit(r, rect)
        y += CARD_SIZE[1]

load_cardset()


class Card(pg.sprite.Sprite, Clickable):
    """docstring for Card"""

    def __init__(self, pos):
        super(Card, self).__init__()
        self.add(BATTLE_SPRITES)

        self.rank = random.choice(CARD_RANKS)
        self.type = random.choice(CARD_TYPE)
        self.face_up = GFX[self.type][self.rank]
        self.face_down = pg.Surface(CARD_SIZE)
        self.face_down.fill((100, 100, 100))
        self.image = self.face_up
        self.rect = self.image.get_rect(center=pos)
        self.mask_rect = self.rect.copy()
        self.mask_rect.center = 0, 0
        self.flip_factor = -1
        self.faceing_up = True
        self.pos = pos
        self.fliping = False
        self.flip_speed = 4
        self.bounce_speed = 1
        self.inx = 0

        # self.message = Button("Hello", (233, 45, 132), (self.rect.right + 10, self.rect.top))
        self.mouse_over = False
        # self.message.handle_click = self.test

        self._side = 'PLAYER'


    def handle_click(self):
        return self.on_click_handler(self.inx)

    def on_click_handler(self, inx):
        '''Maybe not the best way todo it but '''
        return

    def set_defence_pose(self):
        self.image = pg.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center=self.pos)

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
        if(self.faceing_up):
            self.image = self.face_up
        else:
            self.image = self.face_down

    @property
    def side(self):
        return self.side

    @side.setter
    def side(self, side):
        if side != self._side and side in ('PLAYER', 'ENEMIE'):
            self._side = side
            self.face_up = pg.transform.rotate(self.face_up, 180)
            self.face_down = pg.transform.rotate(self.face_down, 180)
            self.image = pg.transform.rotate(self.image, 180)
