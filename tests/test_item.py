import pytest
from src.item import Item


def test_item():
    test1 = Item('test', 1, 2)
    assert test1.name == 'test'
    Item.pay_rate = 2
    test1.apply_discount()
    assert test1.price == 2
    assert test1.calculate_total_price() == 4
