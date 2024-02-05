class Glasses:
    """
    Документация на родительский класс.
    Класс описывает модель очков.
    """
    def __init__(self, brand: str, price: int) -> None:
        """
        Инициализация экземпляра класса.

        :param brand: Бренд очков.
        :param price: Стоимость пары.

        Example:
        >>> glasses = Glasses("Armani", 3000)
        """
        # Применяю protected атрибут brand, поскольку хочу, чтобы клиент купил очки именно в этом магазине
        self._brand = brand
        self. price = price

    def __str__(self) -> str:
        """
        Реализация магического метода __str__.

        return: Строка с названием бренда очков и их стоимостью.

        Example:
        >>> glasses = Glasses("Armani", 3000)
        >>> print(glasses)
        Очки бренда: "Armani". Стоимость: 3000.
        """
        return f'Очки бренда: "{self._brand}". Стоимость: {self.price}.'

    def __repr__(self) -> str:
        """
        Реализация магического метода __repr__.

        return: Строка-инициализатор экземпляра класса.

        Example:
        >>> glasses = Glasses("Armani", 3000)
        >>> print(repr(glasses))
        Glasses("Armani", 3000)
        """
        return f'{self.__class__.__name__}("{self._brand}", {self.price})'


class Sunglasses(Glasses):
    """
    Документация на дочерний класс.
    Класс описывает модель солнцезащитных очков.
    """
    def __init__(self, brand: str, price: int, lens_color: str) -> None:
        """
        Инициализация экземпляра класса.

        :param brand: Бренд очков.
        :param price: Стоимость пары.
        :param lens_color: Цвет линз.

        Example:
        >>> glasses = Sunglasses("Armani", 3000, "Black")
        """
        super().__init__(brand, price)
        self.lens_color = lens_color

    """
    Дополняются магические методы __str__ и __repr__ поскольку
    появился новый атрибут экземпляра класса lens_color.
    """

    def __str__(self) -> str:
        """
        Реализация магического метода __str__.

        return: Строка с названием бренда очков, их стоимостью и цветом линз.

        Example:
        >>> glasses = Sunglasses("Armani", 3000, "Black")
        >>> print(glasses)
        Очки бренда: "Armani". Стоимость: 3000. Цвет линз: "Black".
        """
        return f'Очки бренда: "{self._brand}". Стоимость: {self.price}. Цвет линз: "{self.lens_color}".'

    def __repr__(self) -> str:
        """
        Реализация магического метода __repr__.

        return: Строка-инициализатор экземпляра класса.

        Example:
        >>> glasses = Sunglasses("Armani", 3000, "Black")
        >>> print(repr(glasses))
        Sunglasses("Armani", 3000, "Black")
        """
        return f'{self.__class__.__name__}("{self._brand}", {self.price}, "{self.lens_color}")'

    """Устанавливаю свойство для отличительного атрибута lens_color."""
    @property
    def lens_color(self) -> str:
        return self._lens_color

    @lens_color.setter
    def lens_color(self, lens_color: str) -> None:
        if not isinstance(lens_color, str):
            raise TypeError("Цвет линз должен быть в формате 'str'!")
        if not lens_color:
            raise ValueError("Введите цвет очков!")
        self._lens_color = lens_color


class Visionglasses(Glasses):
    """
    Документация на дочерний класс.
    Класс описывает модель очков для людей с плохим зрением.
    """
    def __init__(self, brand: str, price: int, lens_power: float) -> None:
        """
        Инициализация экземпляра класса.

        :param brand: Бренд очков.
        :param price: Стоимость пары.
        :param lens_power: Оптическая сила линз (диоптрии).

        Example:
        >>> glasses = Visionglasses("Armani", 3000, 2.5)
        """
        super().__init__(brand, price)
        self.lens_power = lens_power

    """
    Дополняются магические методы __str__ и __repr__ поскольку
    появился новый атрибут экземпляра класса lens_power.
    """

    def __str__(self) -> str:
        """
        Реализация магического метода __str__.

        return: Строка с названием бренда очков, их стоимостью и оптической силой линз.

        Example:
        >>> glasses = Visionglasses("Armani", 3000, 2.5)
        >>> print(glasses)
        Очки бренда: "Armani". Стоимость: 3000. Сила линз: 2.5.
        """
        return f'Очки бренда: "{self._brand}". Стоимость: {self.price}. Сила линз: {self.lens_power}.'

    def __repr__(self) -> str:
        """
        Реализация магического метода __repr__.

        return: Строка-инициализатор экземпляра класса.

        Example:
        >>> glasses = Visionglasses("Armani", 3000, 2.5)
        >>> print(repr(glasses))
        Visionglasses("Armani", 3000, 2.5)
        """
        return f'{self.__class__.__name__}("{self._brand}", {self.price}, {self.lens_power})'

    """Устанавливаю свойство для отличительного атрибута lens_power."""

    @property
    def lens_power(self) -> float:
        return self._lens_power

    @lens_power.setter
    def lens_power(self, lens_power: float) -> None:
        if not isinstance(lens_power, float):
            raise TypeError("Оптическая сила линз должна быть переменной типа 'float'")
        if lens_power == 0:
            raise ValueError("У вас хорошее зрение, лучше выбрать солнцезащитные очки!")
        self._lens_power = lens_power


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Write your solution here
    pass
