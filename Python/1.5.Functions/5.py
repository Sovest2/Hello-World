

# def greet(name):
#     """Выводит приветствие по имени человека"""
#     print(f"Привет,{name}. Доброе утро!")


# name = "Олег"
# greet(name)

# print(greet("Виктор Цой"))

# print(greet.__doc__)


# def absolute_value(num):

#     if num >= 0:
#         return num
#     else:
#         return -num


# print(f"Абсолютное значение числа 2: {absolute_value(2)}")
# print(f"Абсолютное значение числа -4: {absolute_value(-4)}")


# def arithmetic (x, y, z):
#     result = 0
#     if z == "+" :
#        result = x + y
#     elif z == "-":
#         result = x - y
#     elif z == "*":
#         result = x * y
#     elif z == "/":
#         if y == 0:
#             result = "Невозможно"
#         else:
#             result = x / y
#     else:
#         return "Неизвестная операция"
#     return f"{x} {z} {y} = {result}"

# x = int(input('Введите первое число : '))
# y = int(input('Введите второе чиcло : '))
# z = input('Введите знак (+, - , *, /) : ')
# print (arithmetic(x, y, z))


# def print_me(string):
#    print(string)

# print_me(string = "Тут должен быть интересный факт, но мы его еще не придумали")


# def print_info(name, age = 50 ):
#    print("Name: ", name)
#    print("Age ", age)

# print_info(age=50, name="Игорь")
# print_info(age=50, name="Андрей" )
# print_info(name="Андрей" )


# def car_trader(model, color = "черный"):
#     return f"Вы купили {model}, цвета: {color} "

# print(car_trader("BMW"))
# print(car_trader("Chevrolet", "Серобурмалиновый"))


# Определение функции
# def print_info(arg1, *args):
#     print(f"Первый аргумент: {arg1}")
#     for var in args:
#         print(var)


# print_info("А.С. Попов")
# print_info("К.Э. Циолковский", "Г.Е. Котельников", "И.И. Ползунов")


# def print_score(*args):
#     if len(args) == 0:
#         print('Зал пуст')
#         return

#     total_score = 0
#     for score in args:
#         total_score += score

#     print(f'Оценка: {total_score / len(args)}')


# print_score(3, 4, 5)


# double = lambda x: x * 2
# print(double(5))


# Задание 1

# money = int(input('Сколько вкладываете: '))
# years = int(input('На сколько лет: '))
# proc = float(input('Процент годовых: '))


# def bank(money, years, percent=6):
#     for i in range(1, years + 1):
#         money += money * (percent / 100)
#         print(f"Год {i}-й. На счету: {money:.2f} рублей")
#     return money


# result = bank(money, years)
# print(f"Всего будет накоплено: {result:.2f}")


# Задание 2

# def pretty_print(header,*actions):
#     line = f"+{'-' * (len(header) + 2)}+"
#     print(line)
#     print(f"| {header} |")
#     print(line)
#     for i in range(len(actions)):
#         print(f"{i} - {actions[i]}")

# pretty_print("Битва", "Ударить", "Блокировать", "Вылечиться", "Пропустить")

