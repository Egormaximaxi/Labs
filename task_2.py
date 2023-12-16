# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separat_=","):  # Задание функции
    first_group.split(separat_)  # Объединение строки через заданный разделитель
    second_group.split(separat_)

    intersection_list = list(set(first_group.split(separat_)).
                             intersection(second_group.split(separat_)))  # Поиск пересечений и присвоение их к списку
    intersection_list.sort()  # Сортировка списка

    return intersection_list  # Вывод списка пересечений


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print("Общие участники для обеих групп:",
      find_common_participants(participants_first_group,
                               participants_second_group, "|"))
