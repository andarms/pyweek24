from random import randint

class Trainer(object):
    """docstring for Trainer"""
    def __init__(self):
        super(Trainer, self).__init__()
        self.lp = 4000
        self.attack = 500
        self.defence = 500
        self.generate_stats()

    def generate_stats(self):
        points = randint(10, 20)        
        while points > 0:
            aumont = randint(1, points) 
            points -= aumont
            aumont *= 100
            aux = randint(1, 3) 
            if aux == 1:
                self.lp += aumont
            elif aux == 2:
                self.attack += aumont
            else:
                self.defence += aumont