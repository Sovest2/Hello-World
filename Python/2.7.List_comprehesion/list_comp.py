# import time
# authors = ['Чехов', 'Достоевский', 'Толстой', 'Тургенев', 'Булгаков']

# start = time.time()
# for author in authors:
#   print(f'{author} + Я = <3')
# end = time.time()
# print(f'1-й: {end - start} seconds')
# print()

# start = time.time()
# [print(f'{author} + Я = <3') for author in authors]
# end = time.time()
# print(f'2-й: {end - start} seconds')
# print()

# start = time.time()
# for i in range(20):
#   if i % 2 == 0:
#     print(f'Число: {i}, квадрат: {i ** 2}')
# end = time.time()
# print(f'3-й: {end - start} seconds')
# print()

# start = time.time()
# [print(f'Число: {i}, квадрат: {i ** 2}') for i in range(20) if i % 2 == 0]
# end = time.time()
# print(f'4-й: {end - start} seconds')


# import random
# new_list = list(range(-500, 500, random.randint(1, 10)))
# filter_list = []
# for i in new_list:
# 	if i % 2 == 0 and i > 0:
# 		filter_list.append(i)
# print(filter_list)

# filter_list = [i for i in new_list if i % 2 == 0 and i > 0]
# print(filter_list)


