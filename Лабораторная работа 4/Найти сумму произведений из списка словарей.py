import json

INPUT_FILE = "input.json"

def task() -> float:
    total = 0
    with open(INPUT_FILE, "r") as file:
        dict_file = json.load(file)
        for dctn in dict_file:
            total += dctn.get("score") * dctn.get("weight")
        total = round(total, 3)
        return total

print(task())
