import pygame as pg

from .scene import Scene

class StatsScene(Scene):
    """docstring for StatsScene"""
    def __init__(self):
        super(StatsScene, self).__init__()
        myfont = pg.font.SysFont('Arial', 30)
        self.textsurface = myfont.render('Some Text', False, (0, 0, 0))


    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((255, 255, 255))
        surface.blit(self.textsurface, (0,0))
