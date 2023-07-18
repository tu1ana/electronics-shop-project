from abc import ABC, abstractmethod

from src.item import Item


class KeyboardLayout:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language:
            self.__language = 'RU'
        else:
            return self.language
        return self


class Keyboard(Item, KeyboardLayout):
    pass
