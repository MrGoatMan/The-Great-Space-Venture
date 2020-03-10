import random

class Blaster(object):

    def __init__(self, player):
        self.player = player
        self.durability = 100
        self.ammo = 10

    def __str__(self):
        return "Blaster owned by " + player

    def fire(self):
        self.ammo -= 1
        self.durability -= randint(5, 10)
