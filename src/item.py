import csv
import os

from src.instantiateCSVerror import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise ValueError('Only able to add together Item and/ or its subclass instances')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        if self.pay_rate < 1.0:
            self.price = self.pay_rate * self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        # path_to_file = os.path.relpath('..//src//items.csv')
        path_to_file = os.path.join(os.path.dirname(__file__), 'items.csv')

        try:
            with open(path_to_file, 'r', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                data = list(reader)
                for line in data:
                    if len(line) != 3:
                        raise InstantiateCSVError
                    else:
                        cls(line['name'], line['price'], line['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        if string.replace('.', '').isdigit() is True:
            return int(float(string))
