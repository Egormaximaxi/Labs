list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

num_players = int(len(list_players) / 2)  # Определение индекса, соотвествующего половине списка

print(list_players[:num_players])
print(list_players[num_players:])
