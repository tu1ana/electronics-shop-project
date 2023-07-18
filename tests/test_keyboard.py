import pytest

from src.keyboard import Keyboard


def test_str():
    k = Keyboard('Dark Project KD87A', 9600, 5)

    assert str(k) == 'Dark Project KD87A'


def test_change_lang():
    k = Keyboard('Dark Project KD87A', 9600, 5)

    assert k.language == 'EN'

    k.change_lang()
    assert str(k.language) == 'RU'

    k.change_lang().change_lang()
    assert str(k.language) == 'RU'
