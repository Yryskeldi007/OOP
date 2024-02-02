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
