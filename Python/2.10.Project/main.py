import os
import datetime

import requests
import json


def get_data_from_url(url):
    responce = requests.get(url)
    if responce.status_code != 200:
        print(f"Недоступен ресурс: {url}")
        exit()
    
    return json.loads(responce.text)

# Получаем данные
todos = get_data_from_url("https://jsonplaceholder.typicode.com/todos")
todos.sort(key=lambda x: x["userId"])
users = get_data_from_url("https://jsonplaceholder.typicode.com/users")
users.sort(key=lambda x: x["id"])

# Подготавливаем директорию
directory = os.path.dirname(__file__) + "/tasks/"
if not os.path.isdir(directory):
    os.mkdir(directory)

# Обработка данных
for user in users:
    # id пользователя
    user_id = user.get("id", -1)
    if user_id <=0:
        print("Пропускаем пользователя с неверным id")
        continue

    # Имя пользователя
    username = user.get("username")
    if not username:
        print(f"Пропускаем пользователя без username(id:{user_id})")
        continue 

    # Первая строка
    name = user.get("name", "Без имени")
    email = user.get("email", "Не указан")
    time = datetime.datetime.now().strftime("%d.%m.%Y %H.%M")
    
    # Вторая строка
    company = user.get("company", {"name": "Не указано"})
    company_name = company.get("name", "Не указано") 

    # Формируем заголовок файла
    content = f"{name} <{email}> {time}\n{company}\n\nЗавершенные задачи:\n"

    # Отбираем задачи
    tasks = []
    todo_id = 0
    while todo_id < len(todos):
        if todos[todo_id].get("userId") != user_id:
            todo_id+=1
            continue

        tasks.append(todos.pop(todo_id))
    
    tasks.sort(key=lambda x: x["completed"], reverse= True)

    # Формируем задачи
    if len(tasks) == 0:
        content+="Без задач\n\nОставшиеся задачи:\nБез задач\n"
    else:
        isDivided = False
        for task in tasks:
            task_name = task.get("title", "Без Имени")
            completed = task.get("completed", False)

            if(not completed and not isDivided):
                content+="\nОставшиеся задачи:\n"
                isDivided = True
            
            content+=f'{task_name[0:50]}{"..." if len(task_name) > 50 else ""}\n'
    
    # Преименовываем старые файлы
    filename = f"{directory+username}.txt"
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = file.readline().replace("\n", "").split(" ")
                data.reverse()
                writen_time = f"{data[0]} {data[1]}"
                previous_time = datetime.datetime.strptime(writen_time, "%H.%M %d.%m.%Y")
        except IOError:
            print(f"Произошла ошибка при переименовывании файла: {filename}")
            continue
        else:
            formated_time = previous_time.strftime("%Y-%m-%dT%H.%M")
            new_filename = f"{directory+username}_{formated_time}.txt"
            os.replace(filename,new_filename)

    # Записываем в файл
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError:
        print(f"Произошла ошибка при записи файла: {filename}")
        if new_filename:
            os.replace(new_filename,filename)