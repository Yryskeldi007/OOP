from art import tprint
class Hello:
    def __init__(self, string):
        self.string = string


class GoodMorning(Hello):
    def art(self):
        tprint('Good Morning' + self.string)


obj = GoodMorning ('teacher')