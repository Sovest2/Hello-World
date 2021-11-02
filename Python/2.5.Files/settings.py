import json
import os

def save_data():
    data ={
        "budget": budget,
        "days": days,
        "money": money,
        "wastes": wastes
    }

    with open(os.path.dirname(__file__) + "/settings.json", "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    global budget
    global days
    global money
    global wastes

    path = os.path.dirname(__file__) + "/settings.json"

    if (not os.path.isfile(path)): 
        return

    with open(path, "r") as file:
        data = json.load(file)
        budget = data.get("budget", 11653)
        days = data.get("days", 31)
        money = data.get("money", round(budget/days, 2))
        wastes = data.get("wastes", [])

budget = 11653
days = 31
money = round(budget/days, 2)
wastes = []

main_window = None