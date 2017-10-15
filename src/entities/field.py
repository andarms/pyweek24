from random import randint
import pygame as pg

from ..bootstrap import SCREEN_SIZE
from .card import Card

ENEMIE_FIELD = [(176, 64), (400, 64), (624, 64), (848, 64)]
PLAYER_FIELD = [(48, 400), (272, 400), (496, 400), (720, 400)]


class Field(object):
    """docstring for Filed"""

    def __init__(self):
        super(Field, self).__init__()
        self.actives = []
        for inx, pos in enumerate(PLAYER_FIELD):
            card = Card(pos)
            card.inx = inx
            # card.handle_click = self.attack
            self.actives.append(card)
        for inx, pos in enumerate(ENEMIE_FIELD):
            card = Card(pos)
            card.side = "ENEMIE"
            card.inx = inx
            # card.handle_click = self.attack
            self.actives.append(card)

        self.rank = 100

    def get_event(self, event):
        for card in self.actives:
            card.get_event(event)

    def attack(self):
        pass


    def generate_triangle(self, surface):
        color = [randint(0, 255) for _ in range(3)]
        x1 = randint(0, SCREEN_SIZE[0])
        y1 = randint(0, SCREEN_SIZE[1])
        x2 = randint(0, SCREEN_SIZE[0])
        y2 = randint(0, SCREEN_SIZE[1])
        x3 = randint(0, SCREEN_SIZE[0])
        y3 = randint(0, SCREEN_SIZE[1])
        pg.draw.line(surface, color, (x1, y1), (x2, y2))
        pg.draw.line(surface, color, (x2, y2), (x3, y3))
        pg.draw.line(surface, color, (x3, y3), (x1, y1))

    def draw(self, surface):
        self.generate_triangle(surface)
        self.generate_triangle(surface)
        self.generate_triangle(surface)
