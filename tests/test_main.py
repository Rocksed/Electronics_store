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

    # test setting product name with property
    item = Item('Смартфон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # test raising exception when product name is too long
    try:
        item.name = 'СуперСмартфон'
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."

    # test creating instances from csv file
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    # test is_integer static method
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False

    def test_item_representation(self):
        item1 = Item("Smartphone", 10000, 20)
        assert str(item1) == "Smartphone"
        assert repr(item1) == "Item('Smartphone', 10000, 20)"

        item2 = Item("Laptop", 50000, 10)
        assert str(item2) == "Laptop"
        assert repr(item2) == "Item('Laptop', 50000, 10)"

