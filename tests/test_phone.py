import pytest

from src.phone import Phone


def test_init_phone():
    phone1 = Phone('Samsung Galaxy S23', 100_000, 20, 2)
    assert phone1.name == 'Samsung Galaxy S23'
    assert phone1.price == 100_000
    assert phone1.quantity == 20
    assert phone1.number_of_sim == 2


def test_repr():
    phone2 = Phone('BlackBerry Bold', 10000, 3, 1)
    assert repr(phone2) == "Phone('BlackBerry Bold', 10000, 3, 1)"


def test_str():
    phone3 = Phone('Nokia 3310', 3000, 2, 1)
    assert str(phone3) == 'Nokia 3310'


def test_number_of_sim():
    phone3 = Phone('Nokia 3310', 3000, 2, 1)
    phone3.number_of_sim = 1

    phone4 = Phone('Rotary_Dial', 1000, 2, 0)
    with pytest.raises(ValueError):
        phone4.number_of_sim = 0
