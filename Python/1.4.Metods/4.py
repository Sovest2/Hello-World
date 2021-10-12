# s = 'Злые языки страшнее пистолета'
# print(s.split())
# s = '              Красота      спасет       мир    '
# print(s.split())
# s = '192.168.1.1'
# print(s.split('.'))
# s = 'Если искать совершенства, то никогда не будешь доволен.'
# print(s.split('и'))
# s = 'A###B###C'
# print(s.split('###'))

# s = ['Тот', 'Кого', 'Нельзя', 'Называть']
# print(''.join(s))
# print(' '.join(s))
# print('-'.join(s))
# print('! '.join(s))
# print(' ААА! '.join(s))

# [1, 2, 3].join([4, 5, 6])

# print(dir([]))

# string = '     дальше будет только сложнее, но у тебя всё получится      '
# print(string.strip().upper().replace('Ё', 'Е'))


# print('мало Средне    МНОГО'.lower().split().index('много'))

# authors = ['Чехов', 'Достоевский', 'Толстой', 'Некрасов', 'Булгаков']

# for i in range(len(authors)):
#   authors.append('Тургенев')
#   print(authors)
#   authors.pop()
#   print(authors)

# for i in range(5):
#   writer = authors.pop()
#   print(authors, writer)

# books = ['Мы']
# for book in range(5):
#   books.append(input('Какую книгу вы положите сверху?: '))
# while books:
#   print('Сегодня вы почитаете книгу: ', books.pop())


# Горизонтальная диаграмма
# nums = input().split()
# for h in nums:
#   print(' '.join('*' * int(h)))


# Вертикальная диаграмма
# Решение 1
# nums = input().split()
# max_n = int(max(nums))

# print('*' * (len(nums) + 2))
# print(f'*{" " * len(nums)}*')

# for h in range(max_n, 0, -1):
#   print('*', end='')

#   for i in range(len(nums)):
#     if int(nums[i]) < h:
#       print(' ', end='')
#     else:
#       print('*', end='')

#   print('*')

# Решение 2
# nums = input().split()
# max_n = int(max(nums))

# print(*['*' for i in range((len(nums) + 2))])
# print(' '.join(f'*{" " * len(nums)}*'))

# string = []

# for h in range(max_n, 0, -1):
#   string.append('*')

#   for i in range(len(nums)):
#     if int(nums[i]) < h:
#       string.append(' ')
#     else:
#       string.append('*')

#   string.append('*')
#   print(*string)
#   string.clear()

