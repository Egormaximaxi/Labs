# TODO Найдите количество книг, которое можно разместить на дискете
num_sheets = 100  # Количество листов в книге
num_str = 50  # Количество строк на листе
num_symb = 25  # Количество символов в строке
memory_for_one_symb = 4  # Память, приходящаяся на один символ в байтах
memory_for_one_book = num_sheets * num_str * num_symb * memory_for_one_symb  # Вес одной книги в байтах
memory_for_one_book_Mb = memory_for_one_book / (2 ** 20)
dics_memory = 1.44   # Объем дискеты в МБайт
num_books = round(dics_memory / memory_for_one_book_Mb)  # Количество книг, помещающихся на дискету

print("Количество книг, помещающихся на дискету:", num_books)
