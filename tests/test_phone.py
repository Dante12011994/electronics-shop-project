import pytest
from src.phone import Phone

def test_phone():
    test1 = Phone('test', 1, 2, 3)
    assert repr(test1) == "Phone('test', 1, 2, 3)"
    test1.number_of_sim = 2
    assert  test1.number_of_sim == 2
