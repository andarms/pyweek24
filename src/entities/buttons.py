import pygame as pg

from ..bootstrap import FONTS


FONT = pg.font.Font(FONTS['west-england.regular'], 20)


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


class Button(Clickable):
    """docstring for Button"""

    def __init__(self, text, color, pos, properties={
            'text_color': (255, 255, 255), 'padding': 10}):
        super(Button, self).__init__()
        self.text = text
        self.color = color
        self._pos = pos
        self.properties = properties
        self.create()

    def create(self):
        self.text_image = FONT.render(
            self.text, False, self.properties['text_color'])
        text_rect = self.text_image.get_rect()
        self.image = pg.Surface(
            (text_rect.width + self.properties['padding']*2, text_rect.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=self._pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text_image, self.rect)

    def handle_click(self):
        print("click")
