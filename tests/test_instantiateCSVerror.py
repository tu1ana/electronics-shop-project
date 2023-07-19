import pytest

from src.instantiateCSVerror import InstantiateCSVError
from src.item import Item


def test_instantiate_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path_to_file='')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path_to_file='../src/broken_items.csv')
