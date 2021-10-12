import this
print("Hello World")
print(137 + 63)
print("137 + 63")
print("137" + "63")
print("Привет, " + "Анатолий")

name = "Анатолий"
print("Привет, " + name)

name = "Татьяна"
print("Привет, " + name)

time = 23
print("Начинаем движение. Осталось идти минут: " + str(time))
time = time - 15
print("Почти пришли. Осталось идти минут: " + str(time))
time = time - 8
print(str(time) + " минут! Вы на месте!")

name = input()
print(name + ", ну как программируется?")


yesterday_steps = ...
today_steps = ...

print(... + ...)


word1 = 'Символы '
word2 = 'в '
word3 = 'кавычках - '
word4 = 'это строки'

text = word1 + word2 + word3 + word4
print(text)


xa = 'ха'
kek = ' так просто'

lol = xa * 5 + kek

print(lol)


film_name = input('Введите название фильма: ')
row = input('Выберите ряд: ')
seat = input('и место: ')
time = input('Время: ')

print(f"Билет на {film_name} в {time} забронирован. Место: {seat}; Ряд: {row}. Приятного просмотра!")


import random

phrases = [
    "пойти покормить кота",
    "погуглить, когда откроют Турцию",
    "читать про зарплаты в Сан-Франциско",
    "попасть в поток грустных песен и вспомнить все ошибки молодости",
    "посмотреть трейлер сериала и, за одно, первый сезон",
    "Юрий Дудь",
    "отправить другу смешной мем",
    "расставить книги в алфавитном порядке"
]

phrase = random.choice(phrases)

print('Не кодить, а ' + phrase)

