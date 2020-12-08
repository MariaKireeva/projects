import random

class Ship:
    def __init__(self, x, y, length, orient=1):
        self.x = x
        self.y = y
        self.length = length
        self.orient = orient
        self.is_dead = False

    def get_status(self):
        return self.is_dead

    def shot(self):
        self.length -= 1
        if self.length == 0:
            self.is_dead = True
        return True

    @property
    def positions(self):
        self.cells = []
        if self.orient:
            for i in range(self.length):
                self.cells.append((self.x + i, self.y))
        else:
            for i in range(self.length):
                self.cells.append((self.x, self.y + i))
        return self.cells


class Board:
    def __init__(self, name):
        self.board = [[i for i in range(1, 7)]] + [[0 for i in range(6)] for i in range(6)]
        self.name = name
        self.all_ships = []
        self.shots = None
        self.forbid_turns = []
        self.problem = []

    def print_board(self):
        for index, line in enumerate(self.board):
            line = list(map(str, line))
            print(index, ' '.join(line))

    def get_winner(self):
        for ship in self.all_ships:
            if not ship.get_status():
                return False
        print(f'\n{self.name} побеждает!\n***********\n\n')
        return True

    def show_ships(self):
        new_board = [[i for i in range(1, 7)]] + [[0 for i in range(6)] for i in range(6)]
        for ship in self.all_ships:
            for position in ship.positions:
                x, y = position
                new_board[x][y] = '■'
        for index, line in enumerate(new_board):
            line = list(map(str, line))
            print(index, ' '.join(line))

    def empty_cell(self, cell):
        if self.all_ships is None:
            return True
        else:
            for ship in self.all_ships:
                if cell in ship.positions:
                    return False
                else:
                    if cell in self.forbid_turns:
                        return False
            return True

    def check_in_field(self, cell):
        x, y = cell
        if x in range(1, len(self.board)) and y in range(0, len(self.board[0])):
            return True
        else:
            return False

    def make_forbid_turns(self, cell):
        x, y = cell
        for row in range(-1, 2):
            for col in range(-1, 2):
                if x + row > 0 and y + col >= 0:
                    if (x + row, y + col) not in self.forbid_turns \
                            and (x + row, y + col) != (x, y):
                        self.forbid_turns.append((x + row, y + col))

    def set_ship(self, *args):
        new_ship = Ship(*args)
        go = []
        for cell in new_ship.positions:
            result = self.empty_cell(cell) and self.check_in_field(cell)
            go.append(result)

        if all(go):
            if self.all_ships is None:
                self.all_ships = []
            self.all_ships.append(new_ship)
            for i, cell in enumerate(new_ship.positions):
                self.make_forbid_turns(cell)
            return True
        else:
            return False

    def ship_dead(self, positions):
        for cell in positions:
            x, y = cell
            for row in range(-1, 2):
                for col in range(-1, 2):
                    if x + row in range(1, len(self.board)) and y + col in range(0, len(self.board[0])) \
                            and ((x + row, y + col) != cell and self.board[x + row][y + col] != 'T' and
                                 self.board[x + row][y + col] != '■'):
                        self.board[x + row][y + col] = '•'

    def user_choice(self):
        while True:
            x = input('\nВыберите ряд - ')
            try:
                x = int(x)
                if x not in range(1, len(self.board)):
                    print()
                else:
                    break
            except ValueError:
                print()
        while True:
            y = input('Выберите колонку - ')
            try:
                y = int(y) - 1
                if y < 0 or y > len(self.board[0]):
                    print()
                else:
                    break
            except ValueError:
                print()
        return x, y

    def shot_user(self):
        while True:
            self.print_board()
            x, y = self.user_choice()
            go = self.shot(x, y)
            if go:
                break
            print('Вы уже стреляли в эту клетку! Надо выбрать другую.\n')

    def shot(self, x, y):
        x, y = x, y
        if self.shots is None:
            self.shots = []
        if (x, y) in self.shots:
            return False
        for ship in self.all_ships:
            if (x, y) in ship.positions:
                print('Попадание!\n')
                self.board[x][y] = 'T'
                ship.shot()
                if ship.get_status():
                    self.ship_dead(ship.positions)
                    print('Корабль убит\n')
                self.shots.append((x, y))
                return True
        print('Мимо!\n')
        self.board[x][y] = '•'
        self.shots.append((x, y))
        return True

    def shot_ai(self):
        while True:
            x, y = (random.randint(1, 6), random.randint(0, 5))
            if self.shots is None:
                self.shots = []
            if (x, y) not in self.shots:
                break
        print(f'{self.name} выбирает клетку - {x},{y + 1}!')
        self.shot(x, y)

    def set_user_deck(self):
        decks = (3, 2, 2, 1, 1, 1, 1)
        for i, deck in enumerate(decks):
            while True:
                print(f'Размещаем корабль {i + 1}. Количество палуб - {deck}.')
                self.show_ships()
                orient = 1
                if deck > 1:
                    while True:
                        orient = input('''Выберите положение для корабля:
                        1 - вниз.
                        0 - вправо.
                        Вы выбираете - ''')
                        try:
                            orient = int(orient)
                            if orient in range(0, 2):
                                break
                            else:
                                print('Ошибка! Вы должны напечатать 1 или 0. Попробуйте снова.')
                        except ValueError:
                            print('Ошибка! Вы должны напечатать 1 или 0. Попробуйте снова.')
                x, y = self.user_choice()
                if self.set_ship(x, y, deck, orient):
                    print('Корабль размещен!\n')
                    break
                else:
                    print('Эта зона занята другим кораблем.')
        print('Все корабли на месте. Начинаем игру.')

    def set_ai_deck(self):
        decks = (3, 2, 2, 1, 1, 1, 1)
        for deck in decks:
            while True:
                x, y = random.randint(1, 6), random.randint(0, 5)
                orient = random.randint(0, 1)
                go = self.set_ship(x, y, deck, orient)
                if go:
                    break


class Game_start:
    def __init__(self):
        self.computer = 'Computer'

    def set_user(self):
        print("*" * 40)
        print(" " * 40)
        print('Добро пожаловать в игру Морской Бой!')
        print(" " * 40)
        print("*" * 40)
        self.user = input('Ваше имя: ')
        print("*" * 40)



    def game(self):
        self.set_user()
        userBoard, compBoard = Board(self.user), Board(self.computer)
        userBoard.set_ai_deck()
        compBoard.set_user_deck()
        user_start = random.randint(0, 1)

        print('\nИгрок будет ходить первым!') if user_start else print('\nКомпьютер будет ходить первым!')
        while True:
            if user_start:
                userBoard.shot_user()
                print('Результат:')
                userBoard.print_board()
                if userBoard.get_winner():
                    break

                compBoard.shot_ai()
                print('Результат:')
                compBoard.print_board()
                if compBoard.get_winner():
                    break
            else:
                compBoard.shot_ai()
                print('Результат:')
                compBoard.print_board()
                if compBoard.get_winner():
                    break
                compBoard.shot_user()
                print('Результат:')
                userBoard.print_board()
                if userBoard.get_winner():
                    break


game = Game_start()
game.game()
