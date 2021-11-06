import json

# file = open ("artists.txt")
# file.close()

# try:
#     # Работа с файлом
#     pass
# finally:
#     # закрытие файла
#     file.close()

# with open ("artists.txt", encoding= "utf-8") as file:

#     print(*file)
#     print(file.read())

#     content = file.read(5)


#     print(content)

#     print(file.read(5))
#     print(file.read(5))

#     print(file.readline())

#     for line in file:
#         print(line, end="")

#     print(file.readlines())

# with open ("songs.txt", "w", encoding= "utf-8") as file:
#     file.writelines(["Veridis Quo", "Robot rock"])

# hobbits = {
#     "Имя": "Бильбо",
#     "Фамилия": "Бэггинс",
#     "Хобби": ["Путешествия", "Писательство"],
#     "Возраст": 111,
#     "Семья": [
#         {
#             "Имя": "Фродо"
#         },
#         {
#             "Имя": "Банго Бэггинс",
#         }
#     ]
# }

# with open("Python/2.5.Files/hobbits.json", "w", encoding="utf-8") as file:
#     json.dump(hobbits, file, ensure_ascii=False, indent=4)

# json_str = json.dumps(hobbits, ensure_ascii=False, indent=4)
# print(json_str)

# with open("Python/2.5.Files/hobbits.json", "r", encoding="utf-8") as file:
#     hobbits = json.load(file)
#     print(hobbits)