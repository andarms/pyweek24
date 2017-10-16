from random import randint
import pygame as pg

from ..bootstrap import SCREEN_SIZE, GFX
from ..core.hud import BATTLE_SPRITES, FloatingLabel, StatInfo
from .buttons import Button
from .card import Card
from .trainer import Trainer


ENEMIE_FIELD = [(240, 152), (464, 152), (688, 152), (912, 152)]
PLAYER_FIELD = [(112, 488), (336, 488), (560, 488), (784, 488)]

CARD_VALUES = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class Field(object):
    """docstring for Filed"""

    def __init__(self):
        super(Field, self).__init__()

        self.image = pg.Surface(SCREEN_SIZE)
        self.rect = self.image.get_rect(topleft=(0, -200))

        self.speed = 10
        self.dist_x = 0
        self.dist_y = 0


        self.player = Trainer()
        self.player.info = StatInfo(self.player, (0,0))
        self.player.info.rect.bottomright = SCREEN_SIZE
        self.enemie = Trainer()
        self.enemie.info = StatInfo(self.enemie, (0,0))

        self.actives = []
        for inx, pos in enumerate(PLAYER_FIELD):
            card = Card(pos)
            card.inx = inx
            card.owner = self.player
            card.on_click_handler = self.card_click_handler
            self.actives.append(card)
        for inx, pos in enumerate(ENEMIE_FIELD):
            card = Card(pos)
            card.side = "ENEMIE"
            card.inx = len(self.actives)
            card.owner = self.enemie
            card.on_click_handler = self.card_click_handler
            self.actives.append(card)

        self.action_buttons = []

        self.rank = 100

        self.phase = "START"

        

        self.ui_buttons = []
        self.attack_phase_button = Button('Test', (16, SCREEN_SIZE[1] - 48))
        self.attack_phase_button.handle_click = self.animate
        self.ui_buttons.append(self.attack_phase_button)

    def get_event(self, event):
        for card in self.actives:
            if card:
                card.get_event(event, (self.rect.x, self.rect.y))
        for button in self.action_buttons:
            button.get_event(event, (self.rect.x, self.rect.y))
        for button in self.ui_buttons:
            button.get_event(event, (self.rect.x, self.rect.y))

    def update(self, dt):
        dx, dy = 0, 0
        if self.rect.x > self.dist_x:
            dx = -self.speed
        if self.rect.x < self.dist_x:
            dx = self.speed
        if self.rect.y < self.dist_y:
            dy = self.speed
        if self.rect.y > self.dist_y:
            dy = -self.speed
        self.rect.x += dx
        self.rect.y += dy

    def card_click_handler(self, index):
        self.select_card = self.actives[index]
        if self.phase == "TARGET_SELECTION":
            self.get_damage(self.attacking_card, self.select_card)
            return
        self.create_action(self.select_card)

    def create_action(self, card):
        self.kill_action_button()
        self.action_buttons = []

        button_attack = Button(
            "Attack", (card.rect.right - 40, card.rect.top + 10))
        button_attack.handle_click = self.start_target_selection

        button_defense = Button("Defend", (button_attack.rect.left,
                                           button_attack.rect.bottom + 10))
        button_defense.handle_click = self.defend
        self.action_buttons.append(button_attack)
        self.action_buttons.append(button_defense)

    def kill_action_button(self):
        for button in self.action_buttons:
            button.kill()

    def start_target_selection(self):
        self.attacking_card = self.select_card
        self.kill_action_button()
        self.phase = "TARGET_SELECTION"

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
        self.image.blit(GFX['field'], (0, 0))
        self.generate_triangle(self.image)
        self.generate_triangle(self.image)
        self.generate_triangle(self.image)
        BATTLE_SPRITES.draw(self.image)

        surface.blit(self.image, self.rect)

    def animate(self):
        if self.rect.y < 0:
            self.dist_y = 0
        else:
            self.dist_y = -200

    # Battle logic
    def get_damage(self, source, target):
        effectiveness = self.get_effectiveness(source, target)
        attack = CARD_VALUES[source.rank] * effectiveness
        defence = CARD_VALUES[target.rank]

        damage = (attack - defence) * 100
        damage = int(damage)
        if damage > 0 : #target damage
            self.actives[target.inx] = None
            target.owner.lp -= damage
            target.owner.info.create()
            target.kill()
            FloatingLabel(str(-damage), target.pos)
        else: # self damage
            self.actives[source.inx] = None
            source.owner.lp -= damage
            source.owner.info.create()
            source.kill()
            FloatingLabel(str(damage), source.pos)

        self.phase = "ATTACK"

    def get_effectiveness(self, source, target):
        if source.type == "GRASS" and target.type == "GRASS":
            return 0.5
        elif source.type == "GRASS" and target.type == "FIRE":
            return 0.5
        elif source.type == "GRASS" and target.type == "WATER":
            return 2
        elif source.type == "FIRE" and target.type == "GRASS":
            return 2
        elif source.type == "FIRE" and target.type == "FIRE":
            return 0.5
        elif source.type == "FIRE" and target.type == "WATER":
            return 0.5
        elif source.type == "WATER" and target.type == "GRASS":
            return 0,5
        elif source.type == "WATER" and target.type == "FIRE":
            return 2
        elif source.type == "WATER" and target.type == "WATER":
            return 0.5
        return 1
