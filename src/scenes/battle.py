import pygame as pg

from ..core.hud import BattleHud, EFFECTS
from ..entities.field import Field
from .scene import Scene


class BattleScene(Scene):
    """docstring for TitleScene"""

    def __init__(self):
        super(BattleScene, self).__init__()
        self.field = Field()
        self.battle_hud = BattleHud()

    def get_event(self, event):
        self.field.get_event(event)

    def update(self, dt):
        self.field.update(dt)
        EFFECTS.update(dt)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.field.draw(surface)
        self.battle_hud.draw(surface)
        EFFECTS.draw(surface)
