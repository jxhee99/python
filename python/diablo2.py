vartest = 5  # 전역변수

def myfun():
    return 'TEST~'

class Amazon:
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15

    def attack(self):
        return '=> Jab'

    def exercise(self):
        self.strength += 2
        self.dexterity += 3
        self.vitality += 1
