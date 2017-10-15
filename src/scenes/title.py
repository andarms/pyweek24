import pygame as pg
from .scene import Scene
from ..entities.card import Card


class TitleScene(Scene):
    """docstring for TitleScene"""

    def __init__(self):
        super(TitleScene, self).__init__()
        self.card = Card((300, 200))

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.card.handle_input(event.pos)

    def update(self, dt):
        self.card.update()

    def draw(self, surface):
        surface.fill((255, 255, 255))
        self.card.draw(surface)
