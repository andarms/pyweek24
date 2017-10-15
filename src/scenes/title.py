import pygame as pg

from ..bootstrap import GFX
from .scene import Scene
from ..entities.card import Card


class TitleScene(Scene):
    """docstring for TitleScene"""

    def __init__(self):
        super(TitleScene, self).__init__()

        self.deck = []
        x = 112
        for i in range(5):
            card = Card((x, 400))
            x += 192
            self.deck.append(card)

    def get_event(self, event):
        for card in self.deck:
            card.get_event(event)

    def update(self, dt):
        for card in self.deck:
            card.update()

    def draw(self, surface):
        surface.blit(GFX['field'], (0, 0))

        for card in self.deck:
            card.draw(surface)
