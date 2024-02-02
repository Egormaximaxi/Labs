# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


class Calendar:
    """
    Документация на класс.
    Класс описывает модель календаря.
    """
    def __init__(self, day: int, month: int, year: int):
        """Инициализация экземпляра класса.

        :param day: День месяца.
        :param month: Месяц.
        :param year: Год.

        Example:
        >>> date = Calendar(2,10,1980)
        """
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("Параметры 'day', 'month' и 'year' должны быть типа 'int' ")
        if day > 31 or day <= 0:
            raise ValueError("Некорректное значение параметра 'day' ")
        if month <= 0 or month > 12:
            raise ValueError("Некорректное значение параметра 'month' ")

        self.day = day
        self.month = month
        self.year = year


    def current_date(self) -> str:
        """ Метод вывыводит на экран текущую дату.

        :return: Строка в формате XX.XX.XXXX

        Example:
        >>> data_ = Calendar(1,11,2020)
        >>> print(data_.current_date())
        Текущая дата: 1.11.2020
        """

        if self.year >= 0:
            return f"Текущая дата: {self.day}.{self.month}.{self.year}"
        else:
            return f"Текущая дата: {self.day}.{self.month}.{- self.year} до н.э."

    def next_day(self) -> int:
        """ Метод позволяет получить следующий за текущим день.

        :return: Число, соотвествующее следующему дню.
        Example:
        >>> data_ = Calendar(30,10,1900)
        >>> print(data_.next_day())
        31
        """
        if self.day == 31:
            return 1
        else:
            return self.day + 1


class Wallet:
    """
    Документация на класс.
    Класс описывает модель кошелька.
    """
    def __init__(self, current_money: Union[int, float], salary: Union[int, float], expenses: Union[int, float]):
        """Инициализация экземпляра класса.

        :param current_money: Текущее кол-во денежных средств в кошельке.
        :param salary: Ежемесячная заработная плата.
        :param expenses: Ежемесячные расходы.

        Example:
        >>> wallet1 = Wallet(1000,80000,50000)
        """

        self.current_money = None
        self.salary = None
        self.expenses = None
        self.init_attrs(current_money, salary, expenses)

    def init_attrs(self, current_money, salary, expenses):

        if not isinstance(current_money, (int, float)):
            raise TypeError("Текущее кол-во средств должно быть числом")
        if not isinstance(salary, (int, float)):
            raise TypeError("З/п должна быть числом")
        if not isinstance(expenses, (int, float)):
            raise TypeError("Расходы должны являться числом")

        if salary < 0:
            raise ValueError("З/п должна быть неотрицательным числом")
        if expenses < 0:
            raise ValueError("Расходы должны быть неотрицательным числом")

        self.current_money = current_money
        self.salary = salary
        self.expenses = expenses

    def is_bankrot(self):
        """Метод определяет период, через который человек с заданными
        финансовыми параметрами станет банкротом (если его доход меньше расходов)."""

    def save_for_goal(self, goal: Union[int, float] = 10**6):
        """ Метод позволяет определить через какой промежуток времени накопится определенная сумма.

        :param goal: Необходимая денежная сумма.
        """


class MovieWebsite:
    """
    Документация на класс.
    Класс описывает модель сайта онлайн-кинотеатра.
    """
    def __init__(self, movie: str, duration: int, subscription: bool):
        """Инициализация экземпляра класса.

        :param movie: Название фильма.
        :param duration: Продолжительность фильма в минутах.
        :param subscription: Наличие активной подписки на сервис.

        Example:
        >>> account1 = MovieWebsite("Метель", 120, True)
        """

        self.movie = None
        self.duration = None
        self.subscription = None
        self.init_account(movie, duration, subscription)

    def init_account(self, movie, duration, subsciption):
        if not isinstance(movie, str):
            raise TypeError("Название фильма должно быть строкой.")
        if not isinstance(duration, int):
            raise TypeError("Продолжительность фильма выражается в целых минутах.")
        if not isinstance(subsciption, bool):
            raise TypeError("Укажите наличие подписки в формате True/False.")
        if movie == "":
            return ValueError("Название фильма не должно быть пустым.")
        if duration <= 0:
            return ValueError("Продолжительность фильма должна быть положительным числом.")

        self.movie = movie
        self.duration = duration
        self.subscription = subsciption

    def sum_duration(self):
        """
        Метод позволяет определелить общую продолжительность просмотра фильмов пользователем.
        """
        ...

    def cost_money(self, traffic: Union[int, float] = 5):
        """
        Метод описывает стоимость просмотра коллекции фильмов без активной подписки.

        :param traffic: Тарифный план установленный на данном сервисе.
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    data = Calendar(1, 11, 2020)
    print(data.current_date())

    wallet_ = Wallet(10000, 100000, 50000)
    print(f"Введенная заработная плата = {wallet_.salary}")

    my_account = MovieWebsite("Герой", 120, True)
    print(f"Вы выбрали для просмотра фильм: '{my_account.movie}', \n его продолжительность: {my_account.duration} мин.")
    pass
