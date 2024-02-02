class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return f'Имя героя:{self.name}'

    def double_health(self):
        self.health_points *= 2
        return f'Удвоенное здоровье:{self.health_points}'

    def __str__(self):
        return f'Прозвище:{self.nickname},\n' \
               f'Суперспособность:{self.superpower},\n' \
               f'Текущее здоровье:{self.health_points}'

    def __len__(self):
        len({self.catchphrase})

# hero = SuperHero('Tick', 'Boss', 'speed', 100, 'go on!')
# print(hero.get_name())
# print(hero.double_health())
# print(hero)
# print(f'Длина фразы:{len(hero.catchphrase)}')


class Hero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=0, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        print(f'Здоровье нашего героя: {self.health_points ** 2}')

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


class SecondHero(SuperHero):
    people = 'people'


thor = Hero('thor', 'bog', 'grom', 200, 'хз', 200)
cap = Hero('cap', 'pon', 'hello', 100, 'Avengers!', 100)

thor.hp()
thor.fly_sky()
cap.hp()
cap.fly_sky()


class Villian(SecondHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self, hero):
        return f'Урон по Таносу: {hero.damage ** 2}'


thanos = Villian('thanos', 'tank', 'stones', 1000, 'destroy')
print(thanos.crit(thor))
print(thanos.crit(cap))