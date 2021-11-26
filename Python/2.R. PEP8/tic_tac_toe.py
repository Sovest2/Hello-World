GAME_TITILE = "Крестики-Нолики"


class TicTacToe:
    def __init__(self):
        self._area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        self._winner = None

    def start_game(self):
        self._gameloop()

    def _print_area(self):
        for line in self._area:
            print(*line)

    def _check_input(self, value: str):
        "Возвращает None если значение не корректно"
        if value.isdigit():
            int_value = int(value) - 1  # Корректировка человеческого ввода
            if 0 <= int_value <= 2:
                return int_value
            else:
                print("Ошибка ввода. Ход пропущен!")
                return
        else:
            print("Ошибка ввода. Ход пропущен!")
            return

    def _check_is_win(self, char):
        "Функция для проверки победы игрока с символом char"
        if (
                self._area[0][0] == char and
                self._area[0][1] == char and
                self._area[0][2] == char):
            return True
        elif (
                self._area[1][0] == char and
                self._area[1][1] == char and
                self._area[1][2] == char):
            return True
        elif (
                self._area[2][0] == char and
                self._area[2][1] == char and
                self._area[2][2] == char):
            return True
        elif (
                self._area[0][0] == char and
                self._area[1][0] == char and
                self._area[2][0] == char):
            return True
        elif (
                self._area[0][1] == char and
                self._area[1][1] == char and
                self._area[2][1] == char):
            return True
        elif (
                self._area[0][2] == char and
                self._area[1][2] == char and
                self._area[2][2] == char):
            return True
        elif (
                self._area[0][0] == char and
                self._area[1][1] == char and
                self._area[2][2] == char):
            return True
        elif (
                self._area[0][2] == char and
                self._area[1][1] == char and
                self._area[2][0] == char):
            return True
        else:
            return False

    def _gameloop(self):
        "Игровой цикл"

        turn_char = ""
        for turn in range(1, 10):
            self._print_area()

            if turn % 2 == 0:
                turn_char = "0"
            else:
                turn_char = "X"

            print(f"Ход №: {turn}\nХодят: {turn_char}")

            # Получение ввода
            row = self._check_input(input("Введите номер строки: "))
            if row is None:
                continue

            column = self._check_input(input("Введите номер столбца: "))
            if column is None:
                continue

            # Выполнение хода
            if self._area[row][column] == "*":
                self._area[row][column] = turn_char
                if self._check_is_win(turn_char):
                    self._winner = turn_char
                    break
            else:
                print("Ячейка занята. Пропуск хода")
                continue

        # Вывод победителя
        if self._winner is not None:
            print(f"Победил игрок {self._winner}")
        else:
            print("Ничья")


continue_ = True

while continue_:
    line = "-" * len(GAME_TITILE)
    print(f"{line}\n{GAME_TITILE}\n{line}")
    game = TicTacToe()
    game.start_game()

    choice = input("Сыграть еще одну?: ")
    if choice.lower().strip() == "нет":
        continue_ = False
