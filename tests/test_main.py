import pytest

from project.main import Item


# test Item class
class TestItem:
    # test __init__ method
    def test_init(self):
        item = Item("Test Item", 10, 5)
        assert item.name == "Test Item"
        assert item.price == 10
        assert item.quantity == 5
        assert item in Item.products

    # test calculate_total_price method
    def test_calculate_total_price(self):
        item = Item("Test Item", 10, 5)
        assert item.calculate_total_price() == 50

    # test apply_discount method
    def test_apply_discount(self):
        item = Item("Test Item", 10, 5)
        assert item.apply_discount(0.2) == 2.0

    # test price_level class attribute
    def test_price_level(self):
        assert Item.price_level == 1
        Item.price_level = 0.9
        assert Item.price_level == 0.9
