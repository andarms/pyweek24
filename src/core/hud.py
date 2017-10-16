import pygame as pg

from ..bootstrap import FONTS, SCREEN_SIZE
from ..entities.trainer import Trainer

BATTLE_SPRITES = pg.sprite.LayeredUpdates()
EFFECTS = pg.sprite.LayeredUpdates()


Font_50 = pg.font.Font(FONTS['west-england.regular'], 50)
Font_30 = pg.font.Font(FONTS['west-england.regular'], 30)
Font_20 = pg.font.Font(FONTS['west-england.regular'], 20)


class FloatingLabel(pg.sprite.Sprite):
    """docstring for FloatingLabel"""
    def __init__(self, text, pos, color=(255, 0, 0)):
        super(FloatingLabel, self).__init__(EFFECTS)
        self.text = text
        self.image = Font_50.render(text, False, color, (0,0,0))
        self.rect = self.image.get_rect(center=pos)
        self.lifespan = 120
        self.speed = 1

    def update(self, dt):
        self.lifespan -= 1
        self.rect.y -= self.speed
        if self.lifespan < 0:
            self.kill()
            del self



class StatInfo(pg.sprite.Sprite):
    """docstring for StatInfo"""
    def __init__(self, trainer, pos):
        super(StatInfo, self).__init__(EFFECTS)
        self.trainer = trainer
        self.pos = pos

        self.image = pg.Surface((160, 64), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect(topleft=self.pos)

        self.create()

    def create(self):
        self.image.fill((0,0,0,0))
        lp_label = Font_30.render('LP: ', False, (255, 255, 255))
        lp_rect = lp_label.get_rect()
        lp = Font_30.render(str(self.trainer.lp), False, (255, 255, 0))

        attack_label = Font_20.render('Atk: ', False, (255, 255, 255))
        attack_rect = attack_label.get_rect()
        attack = Font_20.render(str(self.trainer.attack), False, (255, 255, 255))

        defence_label = Font_20.render('Def: ', False, (255, 255, 255))
        defence_rect = defence_label.get_rect()
        defence = Font_20.render(str(self.trainer.defence), False, (255, 255, 255))

        


        y = 0
        x = 0
        self.image.blit(lp_label, (0, y))
        self.image.blit(lp, (lp_rect.right, y))
        y += lp_rect.bottom
        self.image.blit(attack_label, (0, y))
        self.image.blit(attack, (attack_rect.right, y))
        y += attack_rect.bottom
        self.image.blit(defence_label, (0, y))
        self.image.blit(defence, (defence_rect.right, y))
                        


class BattleHud(object):
    """docstring for BattleHud"""

    def __init__(self):
        
        self.image = pg.Surface(SCREEN_SIZE, pg.SRCALPHA, 32)
        self.image.convert_alpha()
        self.image.fill((0, 0, 0, 0))

        

        








    def draw(self, surface):
        surface.blit(self.image, (0, 0))
