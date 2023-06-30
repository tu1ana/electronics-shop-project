"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


class TestItem:
    pay_rate = 1.0

    def test_calculate_total_price(self):
        item1 = Item('Headset', 4000.0, 50)
        assert item1.calculate_total_price() == 200000.0

    def test_apply_discount(self):
        item1 = Item('Headset', 4000.0, 50)
        assert item1.apply_discount() is None

