from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language


