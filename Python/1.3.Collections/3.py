# n = 0
# for w in 'выхухоль':
#   n += 1
# print(n)

# print(len('выхухоль'))

# word = 'индекс'
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])

# text = 'Гвидо ван Россум'
# vowel_letter = 0  # Гласная буква
# for i in range(len(text)):
#   if text[i] in 'аеиоуыэюя':
#     vowel_letter += 1
# print(vowel_letter)

# print('\u2603')

# print(ord('И'))
# print(chr(1048))

# for i in range(26):
#   print(chr(ord('A') + i))

# Задание 1
# word1 = input('Первое слово: ')
# word2 = input('Второе слово: ')
# if word1[-1] == word2[0]:
#   print('ВЕРНО')
# else:
#   print('НЕВЕРНО')

# Задание 2
# word1 = input('Первое слово: ')
# word2 = input('Второе слово: ')
# while True:
#   if word1[-1] != word2[0]:
#     print(word2)
#     break
#   word1 = word2
#   word2 = input('Следующее слово: ')

# word1 = input('Первое слово: ')
# word2 = input('Второе слово: ')
# while word1[-1] == word2[0]:
#   word1 = word2
#   word2 = input('Следующее слово: ')
# print(word2)

# Задание 3
# message = input()
# n = int(input())
# if n > 0:
#   print(message[n-1])
# else:
#   print('ОШИБКА')

# Задание 4
# n = int(input('Шаг: '))
# word = input('Послание: ')
# answer = ''
# upper = False
# for char in word:
#     # Если символ в верхнем регистре
#     if 1040 <= ord(char) <= 1071:
#         upper = True  # Помечаем
#     elif 1072 <= ord(char) <= 1103:
#         upper = False

#     symb = ord(char) + n  # Шаг

#     # Если "перешагули" порог
#     if not (1040 <= symb <= 1103):
#         symb = chr(symb - 32)  # возвращаемся в начало
#         # Если этого не хватило, значит перед нами знак препинания или др. символ
#         if not (1040 <= ord(symb) <= 1103):
#             symb = char  # Тогда ничего не меняем
#     else:
#         # Если заглавная буква ушла в зону строчных букв
#         if upper is True and not (1040 <= symb <= 1071):
#             symb = chr(symb - 32)  # Возвращаем ее на место
#         else:
#             symb = chr(symb)  # А на нет и суда нет ))

#     answer += symb  # Собираем строку
# print(answer)

# number = input()
# first = second = 0
# for i in range(0, len(number), 2):
#   first += int(number[i])
# for i in range(1, len(number), 2):
#   second += int(number[i])
# if first == second:
#   print('Счастливый по-питерски!')
# else:
#   print('Несчастливый :(')

# text = 'Hello, world!'
# print(text[0:5])
# print(text[7:12])

# text = 'Hello, world!'
# print(text[:5])
# print(text[7:])

# full_name = 'Васильев А.А.'
# surname = full_name[:-4]
# print(surname)

# number = input()
# first = second = 0
# # срез будет от начала строки до конца с шагом два: 0, 2, 4,...
# for n in number[::2]:
# 	first += int(n)
# # срез от второго элемента строки до конца с шагом два: 1, 3, 5,...
# for n in number[1::2]:
# 	second += int(n)
# if first == second:
# 	print('Счастливый по-питерски!')
# else:
#   print('Несчастливый :(')

# a = 'Python'
# print(a[2:10000])
# print(a[999:])

# text = 'СЕЛ В ОЗЕРЕ БЕРЕЗОВ ЛЕС'
# text_reversed = text[::-1]
# print(text == text_reversed)
# print(text_reversed)

# Списки
# new_list = []
# new_list = list()
# authors = ['Чехов', 'Достоевский', 'Толстой', 'Некрасов', 'Булгаков'] * 4
# authors = ['Чехов', 'Достоевский', 'Толстой', 'Некрасов', 'Булгаков']
# print(authors)

# nums = [0] * 4
# print(nums)

# print(f'{authors[0]} и {authors[2]} дружили какое-то время')

# print(authors[999])

# authors[3] = 'Гоголь'
# print(authors)

# authors.append('Пастернак')
# print(authors)
# poets = ['Пушкин', 'Есенин', 'Блок']
# authors.extend(poets)
# print(authors)
# print(authors + poets)
# authors += poets
# print(authors)

# primes = [2, 3, 5, 7, 11]
# for i in range(len(primes)):
#     print(f'Простое число номер {i+1} - {primes[i]}')
# for p in primes:
#     print(f'Квадрат числа {p} - {p ** 2}')


# n = 10
# a = []
# print(f'Введите {n} значений: ')
# for i in range(n):
#     a.append(input())
# print('Получился список строк:', a)

# months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
          # 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# spring = months[2:5]
# for month in spring:
#     print(month)

# months[5:8] = ['June', 'July', 'August']

# print(months)

# a = [1, 2, 3, 4, 5, 6]
# del a[2]
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# del a[::2]
# print(a)

# Задание 1. Белый список
# n = int(input())
# white_list = []
# for i in range(n):
#     white_list.append(input())

# k = int(input())
# for i in range(k):
#     search = input()
#     if search in white_list:
#         print(search)


# Задание 2. Дед поисковых систем
# n = int(input())
# data = []
# for i in range(n):
#     search = input()
#     data.append(search)

# word = input()
# for line in data:
#     if word in line:
#         print(line)


# Задание 3. Только без лука
# n = int(input())
# recipe = []
# for i in range(n):
#     string = input('Рецепт: ')
#     if 'лук' not in string:
#         recipe.append(string)

# print(*recipe, sep=', ')