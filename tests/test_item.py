import pytest
from src.item import Item


def test_item():
    test1 = Item('test', 1, 2)
    assert test1.name == 'test'
    Item.pay_rate = 2
    test1.apply_discount()
    assert test1.price == 2
    assert test1.calculate_total_price() == 4
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    test1.name = 'Смартфон'
    assert test1.name == 'Смартфон'
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
