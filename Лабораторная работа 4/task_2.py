# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Функция конвертера CSV ->JSON"""
    with open(INPUT_FILENAME) as f:
        rows = [lines for lines in csv.DictReader(f)]  # Дисериализация файла в формате столбец - значение

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(rows, indent=4))  # Запись в выходной файл сереализованных данных


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
