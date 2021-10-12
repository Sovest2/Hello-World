# Множества
# data_types = {'bool', 'str', 'int', 'float', 'list', 'set'}
# print(data_types)

# empty = set()
# print(empty)

# mammals_and_numbers = {'cat', 5, 'dog', 3, 'fox', 12, 'elephant', 4}
# print(mammals_and_numbers)
# print(mammals_and_numbers)
# print(mammals_and_numbers)

# jedies = {'падаван', 'рыцарь', 'магистр', 'падаван'}
# print(jedies)

# for jedi in jedies:
#   print(jedi)

# if 'ситх' in jedies:
#   print('OK')
# else:
#   print('Ну, привет. Пжжжжжж.. (с) Оби-Ван')

# veider = 'Энакин'
# jedies.add(veider)

# print(jedies)

# jedies.discard('падаван')
# jedies.discard('Палпатин')
# jedies.remove('Энакин')
# print(jedies)
# jedies.remove('Асока')

# print('до удаления:', jedies)
# elem = jedies.pop()
# print('удалённый элемент:', elem)
# print('после удаления:', jedies)

# jedies.clear()
# print(jedies)

# sith = {'Палпатин', 'Дарт Вейдер', 'Дарт Мол', 'Граф Дуку', 'Энакин'}
# print(jedies)
# union = jedies.union(sith)
# union = jedies | sith
# print(union)

# intersection = jedies.intersection(sith)
# intersection = jedies & sith
# print(intersection)

# print(jedies <= jedies)
# print(intersection <= jedies)
# print(sith <= jedies)


# Словари
# profile = dict()
# profile = {}

# profile["имя"] = "Джонни Сильверхенд"
# print(profile)
# print(profile["имя"])
# print(profile["им"+"я"])
# print(profile["Дата рождения"])
# print(profile.get("Дата рождения"))
# print(profile.get("Дата рождения","Никто не знает :("))
# profile["статус"] = "Прекрасный день, чтобы уничтожить Арасаку"
# print(profile)
# profile["статус"] = "Наконец- то, впервые за много лет с друзьями провели концерт!"
# print(profile.get("статус"))
# profile.update({"имя": "Ви", "статус": "Кажется, мне становится с каждым разом все хуже и хуже"})
# print(profile)
# del profile["статус"]
# print(profile.pop("статус"))
# print(profile)
# print(profile.pop("город", None))

# if "имя" in profile:
#     print('Мы знаем его имя!')

# if "instagram" not in profile:
#     print('Кажется, он не очень то любит фотографироваться!')

# print(profile.keys())
# print(profile.values())

# for key in profile:
#     print(key)

# for key, value in profile.items():
#     print(f"{key}: {value}")

# profile.clear()
# print(profile)

# Задание 1
# places = dict()
# n = int(input("Сколько концертов проведено: "))

# for i in range(n):
#     concert = input("Дата и место концерта: ").split("|")
#     date = concert[0]
#     place = concert[1]

#     if place in places:
#         places[place].append(date)
#     else:
#         places[place] = [date]

# m = int(input("Сколько мест проверить: "))
# check_places = []
# for i in range(m):
#     place = input("Место: ")
#     check_places.append(place)


# for place in check_places:
#     if place in places:
#         dates = places.get(place)
#         print(f"{place} - ", *dates)
#     else:
#         print()


# Задание 2
# words = dict()

# text = input("Расскажи историю: ")

# for word in text.split(" "):
#     if word in words:
#         words[word] += 1
#     else:
#         words[word] = 1


# for word, value in words.items():
#     print(f"{word} - {value}")
