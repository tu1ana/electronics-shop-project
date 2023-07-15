from abc import ABC, abstractmethod

from src.item import Item


class KeyboardLayout(ABC):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @abstractmethod
    def change_lang(self):
        pass


class Keyboard(Item, KeyboardLayout):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def __str__(self):
        return self.name

    def change_lang(self):
        if self.__language:
            self.__language = 'RU'
        else:
            return self.language
        return self

    @property
    def language(self):
        return self.__language
