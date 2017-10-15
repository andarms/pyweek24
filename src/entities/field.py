from .card import Card

ENEMIE_FIELD = [(176, 64), (400, 64), (624, 64), (848, 64)]
PLAYER_FIELD = [(48, 400), (272, 400), (496, 400), (720, 400)]


class Field(object):
    """docstring for Filed"""

    def __init__(self):
        super(Field, self).__init__()
        for pos in PLAYER_FIELD:
            card = Card(pos)
        for pos in ENEMIE_FIELD:
            card = Card(pos)
