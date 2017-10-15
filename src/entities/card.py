import random
import pygame as pg

CARD_SIZE = (200, 300)


class Card(pg.sprite.Sprite):
    """docstring for Card"""

    def __init__(self, pos):
        super(Card, self).__init__()
        self.face_up = pg.Surface(CARD_SIZE)
        self.face_up.fill([random.randint(0, 255) for _ in range(3)])
        self.face_down = pg.Surface(CARD_SIZE)
        self.face_down.fill([random.randint(0, 255) for _ in range(3)])
        self.rect = self.face_up.get_rect(topleft=pos)
        self.mask_rect = self.rect.copy()
        self.mask_rect.topleft = 0, 0
        self.flip_factor = -1
        self.faceing_up = False
        self.pos = pos
        self.fliping = False
        self.flip_speed = 4
        self.bounce_speed = 1

    def handle_input(self, mouse_pos):
        if self.fliping:
            return
        if mouse_pos[0] >= self.rect.x and \
            mouse_pos[0] <= self.rect.x + self.rect.width and \
            mouse_pos[1] >= self.rect.top and \
            mouse_pos[1] <= self.rect.top + self.rect.height:
            self.fliping = True

    def update(self):
        if self.fliping:
            self.mask_rect.width += self.flip_speed * self.flip_factor
            self.rect.x = self.pos[0] + \
                (self.rect.width - self.mask_rect.width) // 2
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
        # surface.blit(self.image, self.rect)
