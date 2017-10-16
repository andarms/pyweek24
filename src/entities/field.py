from random import randint
import pygame as pg

from ..bootstrap import SCREEN_SIZE
from .buttons import Button
from .card import Card

ENEMIE_FIELD = [(240, 152), (464, 152), (688, 152), (912, 152)]
PLAYER_FIELD = [(112, 488), (336, 488), (560, 488), (784, 488)]


class Field(object):
    """docstring for Filed"""

    def __init__(self):
        super(Field, self).__init__()
        self.actives = []
        for inx, pos in enumerate(PLAYER_FIELD):
            card = Card(pos)
            card.inx = inx
            card.on_click_handler = self.attack
            self.actives.append(card)
        for inx, pos in enumerate(ENEMIE_FIELD):
            card = Card(pos)
            card.side = "ENEMIE"
            card.inx = len(self.actives)
            card.on_click_handler = self.attack
            self.actives.append(card)

        self.buttons = []

        self.rank = 100

    def get_event(self, event):
        for card in self.actives:
            card.get_event(event)
        for button in self.buttons:
            button.get_event(event)

    def attack(self, index):
        self.select_card = self.actives[index]
        self.create_action(self.select_card)

    def create_action(self, card):
        for button in self.buttons:
            button.kill()
        self.buttons = []
        button1 = Button("Attack", (card.rect.right - 40 , card.rect.top + 10))
        button2 = Button("Defend", (button1.rect.left, button1.rect.bottom + 10))
        button2.handle_click = self.defend
        self.buttons.append(button1)
        self.buttons.append(button2)

    def defend(self):
        self.select_card.set_defence_pose()
        self.create_action(self.select_card)

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
