import csv
import os
class InstantiateCSVError(Exception):
    pass

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
        self.price = int(price)
        self.quantity = int(quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls):
        try:
            open(os.path.join('..', 'src', 'items.csv'))
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')
        else:
            with open(os.path.join('..', 'src', 'items.csv')) as file:
                file = csv.DictReader(file)
                for i in file:
                    if len(i) != 3:
                        raise print('InstantiateCSVError: Файл item.csv поврежден')
                    else:
                        Item.all.append(cls(i['name'], i['price'], i['quantity']))

    @staticmethod
    def string_to_number(num):
        return int(float(num))

    # def instantiate_from_csv(self):
    #     try:
    #         open(os.path.join('..', 'src', 'items.csv'))
    #     except FileNotFoundError:
    #         print("Файл не существует")
