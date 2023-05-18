import pytest
from src.keyboard import Keyboard


def test_keyboard():
    test1 = Keyboard("test", 1, 2)
    test1.change_lang()
    assert test1.language == "RU"
    test1.change_lang()
    assert test1.language == "EN"
