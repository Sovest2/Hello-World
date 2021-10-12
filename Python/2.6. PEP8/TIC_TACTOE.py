game_title = "Крестики-Нолики"

class tic_tac_toe:
    def __init__( me ):
        me._area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        me._winner = None



    def start_game( me ):
        me._gameloop()



    def _print_area( me ):
        for line in me._area:
            print(*line)
    


    def _check_input ( me , znachenie: str ) :
        "Возвращает None если значение не корректно"
        if znachenie.isdigit () :
            int_znachenie=int ( znachenie )-1 #Корректировка человеческого ввода
            if 0  <=  int_znachenie  <=  2 :
                return int_znachenie
            else :
                print ( "Ошибка ввода. Ход пропущен!" )
                return
        else :
            print ( "Ошибка ввода. Ход пропущен!" )
            return
    


    def _check_is_win( me, char ):
        "Функция для проверки победы игрока с символом char"
        if (me._area[0][0] == char and me._area[0][1] == char and me._area[0][2] == char):
            return True
        elif (me._area[1][0] == char and me._area[1][1] == char and me._area[1][2] == char):
            return True
        elif (me._area[2][0] == char and me._area[2][1] == char and me._area[2][2] == char):
            return True
        elif (me._area[0][0] == char and me._area[1][0] == char and me._area[2][0] == char):
            return True
        elif (me._area[0][1] == char and me._area[1][1] == char and me._area[2][1] == char):
            return True
        elif (me._area[0][2] == char and me._area[1][2] == char and me._area[2][2] == char):
            return True
        elif (me._area[0][0] == char and me._area[1][1] == char and me._area[2][2] == char):
            return True
        elif (me._area[0][2] == char and me._area[1][1] == char and me._area[2][0] == char):
            return True
        else:
            return False
    

    
    def _gameloop( me ):
        "Игровой цикл"

        turn_char = ""
        for turn in range(1,10):
            me._print_area()

            if turn % 2 == 0:
                turn_char = "0"
            else:
                turn_char = "X"

            print(f"Ход №: {turn}\nХодят: {turn_char}")

            #Получение ввода
            row = me._check_input(input("Введите номер строки: ")) 
            if row == None:
                continue

            column = me._check_input(input("Введите номер столбца: ")) 
            if column == None:
                continue

            #Выполнение хода
            if me._area[row][column] == "*":
                me._area[row][column] = turn_char
                if me._check_is_win(turn_char):
                    me._winner = turn_char
                    break
            else:
                print("Ячейка занята. Пропуск хода")
                continue
        
        #Вывод победителя
        if me._winner != None:
            print(f"Победил игрок {me._winner}")
        else:
            print("Ничья")



continue = True

while continue:
    line = "-" * len(game_title)
    print(f"{line}\n{game_title}\n{line}")
    game = tic_tac_toe()
    game.start_game()

    choice = input("Сыграть еще одну?: ")
    if choice.lower().strip() == "нет":
        continue = False
