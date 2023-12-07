numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_new = numbers[0:4] + numbers[5:]  # Задание нового списка с искл
sum_numbers_new = sum(numbers_new)  # Сумма чисел списка за исключением пропуска
count_numbers = len(numbers)  # Количество чисел (элементов списка)
average_numbers = sum_numbers_new / count_numbers
numbers[4] = average_numbers

print("Измененный список:", numbers)
