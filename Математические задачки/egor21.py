from time import sleep
from random import randint


class Hero():
    def __init__(self, name, live, atak, arsenal):
        self.name = name
        self.live = live
        self.atak = atak
        self.arsenal = arsenal

    def print_info(self):
        print('Имя:', self.name)
        print('Здоровье:', self.live)
        print('Атака:', self.atak)
        print('Оружие:', self.arsenal, '\n')

    def battle(self, enemy):
        print(enemy.name, 'получает сильный удар \nТекущий уровень здоровья:', enemy.live, '\n')
        sleep(3)

    '''def strike(self, enemy):
        print(self.name, 'НАНОСИТ УДАРРР!!!!!!', self.name, 'с силой', self.atak, 'используя', self.arsenal, '\n')
        enemy.live -= self.atak
        self.battle(enemy)'''


class Knight(Hero):
    def __init__(self, name, live, atak, arsenal, armor):
        super(). __init__(name, live, atak, arsenal)
        self.armor = armor
    def strike(self, enemy):
        print('Доблесный рыцарь', self.name, 'взмахивает своим', self.arsenal, 'нанося сокрушительныйудар по ', enemy.name)
        enemy.live -= self.atak
    def defence(self, enemy):
        self.armor -= enemy.atak
        if self.armor <= 0:
            self.live += self.armor
            self.armor = 0            
        print('Текущий уровень брони:', self.armor, '\n')

class Skelet(Hero):
    def __init__(self, name, live, atak, arsenal, magic):
        super(). __init__(name, live, atak, arsenal)
        self.magic = magic
    def strike(self, enemy):
        print('Злой скелет', self.name, 'использует свою', self.arsenal, 'создавая и нанося удар камнями по', enemy.name)
        half = randint(0, 2)
        self.atak += half
        print(self.name, 'увеличил свою силу на', half)
        print('Текущий уровень силы:', self.atak)
        enemy.live -= self.atak
        self.battle(enemy)
               
class Witch(Hero):
    def strike(self, enemy):
        half = randint(0, 5)
        self.live += half
        print(self.name, 'воскресила себе', half, 'жизней')
        print('Текущий уровень здоровья:', self.live)
        print('Злая ведьма', self.name, 'взмахивает своим', self.arsenal, 'нанося сокрушительный удар по', enemy.name, '\n')
        enemy.live -= self.atak
        self.battle(enemy)

karl = Knight('Карл', 40, 5, 'мeч', 15)
bob = Skelet('Боб', 40, 1, 'магия', 'усиление')
luisa = Witch('Луиза', 50, 4, 'посох')

karl.print_info()
bob.print_info()
luisa.print_info()



while bob.live >= 0 or luisa.live >= 0:
    if bob.live >= 0:
        bob.strike(luisa)
        if luisa.live <= 0:
            print('Победил в этой грандиозной битве: Бооооооооб!')
            break

    if luisa.live >= 0:
        luisa.strike(bob)
        if bob.live <= 0:
            print('Победила в этой грандиозной битве: Луизаааааа!')
            break

