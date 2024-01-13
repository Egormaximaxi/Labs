# TODO решите задачу
import json


def task() -> float:
    """Функция для поиска суммы произведений из списка словарей"""""
    with open("input.json") as f:
        json_data = json.load(f)  # Десериализация файла
        sum_ = sum([i["score"] * i["weight"] for i in json_data])
    return round(sum_, 3)


print(task())
