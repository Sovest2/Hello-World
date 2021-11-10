import json
import os

def save_data():
    data ={
        "budget": budget,
        "days": days,
        "money": money,
        "wastes": wastes,
        "last_date": last_date
    }

    with open(os.path.dirname(__file__) + "/settings.json", "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    global budget
    global days
    global money
    global wastes
    global last_date

    path = os.path.dirname(__file__) + "/settings.json"

    if (not os.path.isfile(path)): 
        return

    with open(path, "r") as file:
        data = json.load(file)
        budget = data.get("budget", 11653)
        days = data.get("days", 31)
        money = data.get("money", round(budget/days, 2))
        wastes = data.get("wastes", [])
        last_date = data.get("last_date")

def update_date(difference):
    global days
    global budget
    global money

    budget+=  money - round(budget/days, 2)
    days-= difference
    money = round(budget/days, 2)

budget = 11653
days = 31
money = round(budget/days, 2)
wastes = []
last_date = None

main_window = None