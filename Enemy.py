import pygame

class Enemy():
    def __init__(self, name, hp, dmg, exp_to_drop):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.exp_to_drop = exp_to_drop
    
    def is_alive(self):
        return self.hp > 0
    
    def take_dmg(self, player_dmg):
        self.hp = self.hp - player_dmg

    def is_dead(self):
        if self.hp == 0:
            print(f'{self.name} был убит')
    
    def drop_exp(self, player_exp):
        if Enemy.is_dead() == True:
            player_exp += self.exp_to_drop
    
    def patrooling():
        pass