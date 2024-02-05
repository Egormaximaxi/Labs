class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    #  Поскольку в дочернем классе появился новый атрибут, то рекомендуется перегрузить методы __str__ и __repr

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:

        if not isinstance(pages, int):
            raise TypeError("Число страниц должно быть целым числом!")
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным числом!")

        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    #  Поскольку в дочернем классе появился новый атрибут, то рекомендуется перегрузить методы __str__ и __repr

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:

        if not isinstance(duration, float):
            raise TypeError("Некорректный тип данных переменной 'duration'!")
        if duration < 0:  # 0 не включительно, поскольку тип переменной float не принимает 0
            raise ValueError("Значение переменной 'duration' должно быть положительным!")

        self._duration = duration


book_1 = PaperBook("Евгений Онегин", "Пукшин", 500)
book_2 = AudioBook("Тихий Дон", "Шолохов", 52.5)

print(book_1)
print(repr(book_2))
