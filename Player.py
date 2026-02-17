class Player():
    def __init__(self, name, hp, dmg, lvl, exp):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.lvl = lvl
        self.exp = exp
    
    def is_alive(self):
        return self.hp > 0
    
    def lvl_up(self):
        self.lvl += 1
        print(f'{self.name} повысил уровень до {self.lvl}')
    
    def gain_exp(self, k): # k - количество получаемого опыта, увеличавающегося для увеличения сложности получения уровня
        while self.exp > k:
            self.exp -= k
            Player.lvl_up()
    
    def take_dmg(self, enemy_dmg):
        self.hp = self.hp - enemy_dmg

    def move():
        pass