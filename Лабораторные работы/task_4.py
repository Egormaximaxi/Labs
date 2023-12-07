users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

stat_website = {"Общее количество": 0,
                "Уникальные посещения": 0
                }  # Создание словаря
total_visits = len(users)  # Определение общего количества посещений
unique_set = set(users)  # Создание множества для определения уникальных посещений
unique_visits = len(unique_set)  # Определение количества уникальных посещений
stat_website["Общее количество"] = total_visits  # Присвоение значений словарю
stat_website["Уникальные посещения"] = unique_visits

print(stat_website)