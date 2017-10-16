import pygame as pg

from .scene import Scene
from ..entities.field import Field


class TitleScene(Scene):
    """docstring for TitleScene"""

    def __init__(self):
        super(TitleScene, self).__init__()
        self.field = Field()
        self.deck = []

    def get_event(self, event):
        self.field.get_event(event)

    def update(self, dt):
        self.field.update(dt)

    def draw(self, surface):
        surface.fill((255, 255, 255))
        self.field.draw(surface)
