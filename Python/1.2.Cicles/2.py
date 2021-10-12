# Кассовый аппарат
# Как работает:
# 1. На вход подается товар (стоимость)
# 2. Если цена товара больше 1000 рублей, то применяется скидка 5%.
# 3. Вывести сумму стоимости всех товаров с учетом скидок.

# num = 10
# while num > 0:
#   print(f'Обратный отсчет: {num}')
#   num -= 1


# sum = 0
# cost = 1
# while cost > 0:
#   cost = float(input('Стоимость товара: '))
#   if cost > 1000:
#     cost = cost - cost * 0.10
#   sum = sum + cost

# print(f'Сумма стоимости всех товаров: {sum:.2f} рублей')

# Задание 1
# num = int(input('Число: '))

# while num >= 0:
#   if num % 2 == 0:
#     print('Четное')
#   else:
#     print('Нечетное')
#   num = int(input('Число: '))


# for i in range(5):
#   print('Белки умеют мурчать')

# print(list(range(99)))

# range(5, 101, 5)

# Отладка
# for num in range(1, 34):
#   print(f'{num}-й попугай')

# word = 'Лучше простое, чем сложное'
# for w in word:
#   print(w, end=' :) ')

# zen_of_python = [
#     'Сложное лучше, чем запутанное', 'Плоское лучше, чем вложенное',
#     'Явное лучше, чем неявное', 'Особые случаи не настолько особые, чтобы нарушать правила',
#     'При этом практичность важнее безупречности',
#     'Должен существовать один и, желательно, только один очевидный способ это сделать ',
#     'Если реализацию сложно объяснить — идея плоха'
# ]
# for rule in zen_of_python:
#     print(rule)


# import random
# words = ["семечки", "ташкент", "небывалый","животворящий", "чахохбили", "ризотто"]
# word = random.choice(words)
# letters = []
# HP = 3

# while HP > 0:
#   victory = True
#   letter = input('Введите букву: ')
#   letters.append(letter)  # Добавление букв в список букв
#   print(letters)          # Вывод списка для наглядности
#   for char in word:
#     if char in letters:
#       print(char, end=' ')
#     else:
#       print('*', end=' ')
#       victory = False
#   print()

#   if letter not in word:
#     HP -= 1
#     print(f'Такой буквы нет в слове. У вас осталось {HP} HP')

#   if HP == 0:
#     print('Gameover!')

#   if victory == True:
#     print('Слово угадано.')
#     break               # Останавливает работу цикла

# ДЗ 1
# secs = int(input('Сколько секунд до пуска ракеты: '))
# for i in range(secs, - 1, -1):
#   print(f"Осталось секунд: {i}")
# print("Пуск")

# ДЗ 2
# t = 0.0
# day = 0
# while t < 22.0:
#   t = float(input('t: '))
#   day += 1
# print(day // 7)

# ДЗ 3
# n = int(input())
# for i in range(1, n + 1):
#   spaces = (n - i) * ' '
#   asterisks = i * '*' + (i - 1) * '*'
#   print(f'{spaces}{asterisks}')

# ДЗ 4
# num = int(input())
# simple = 0
# simples = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         simple += 1
#         simples.append(i)

# print(*simples)
# if simple == 2:
#     print("ПРОСТОЕ")
# else:
#     print("НЕТ")
