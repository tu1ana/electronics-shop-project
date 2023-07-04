"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


class TestItem:

    def test_calculate_total_price(self):
        item1 = Item('Headset', 4000.0, 50)
        assert item1.calculate_total_price() == 200000.0

    def test_apply_discount(self):
        Item.pay_rate = 0.6
        item1 = Item('Headset', 4000.0, 50)
        assert item1.apply_discount() is None
        assert Item('Headset', 2400.0, 50)

    def test_name_not_more_than_ten_symbs(self):
        item = Item('Смартфон', 10000, 5)
        item.name = 'Смартфон'
        assert item.name == 'Смартфон'
        item1 = Item('Motherboard', 5000, 8)
        item1.name = 'Motherboard'
        assert item1.name == 'Motherboar'

    def test_instantiate_from_csv(self):
        Item.all = []
        Item.instantiate_from_csv()
        assert len(Item.all) == 5
        item = Item.all[0]
        assert item.name == 'Смартфон'


@pytest.mark.parametrize('value, expected', [('5', 5), ('5.0', 5), ('5.5', 5)])
def test_string_to_number(value, expected):
    assert Item.string_to_number(value) == expected
