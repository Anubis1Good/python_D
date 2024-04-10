class Player():
    counter = 0 #статическое свойство

    def __init__(self,name):
        self.name = name #свойство экземпляра
        Player.counter += 1

    @staticmethod #статический метод
    def amount_players():
        print('Всего игроков:',Player.counter)


p1 = Player('Ivan')
p2 = Player('Oleg')
p3 = Player('Elena')

print(Player.name) # AttributeError
print(p1.name) # Ivan
print(Player.counter) # вывод 3
Player.amount_players() # Всего игроков: 3



