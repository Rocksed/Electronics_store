import pytest
from project.main import Item, Phone, Keyboard


def test_item_instantiation():
    item1 = Item("Laptop", 1000, 1)
    assert item1.name == "Laptop"
    assert item1.price == 1000
    assert item1.quantity == 1


def test_item_name_setter():
    item2 = Item("Monitor", 500, 2)
    item2.name = "TV"
    assert item2.name == "TV"
    with pytest.raises(Exception):
        item2.name = "Smartphone with a very long name"


def test_item_calculate_total_price():
    item3 = Item("Mouse", 50, 3)
    Item.price_level = 2
    assert item3.calculate_total_price() == 300


def test_item_apply_discount():
    item4 = Item("Keyboard", 200, 1)
    assert item4.apply_discount(0.2) == 40.0


def test_item_instantiate_from_csv():
    Item.instantiate_from_fcsv()
    assert len(Item.all) == 4


def test_phone_instantiation():
    phone1 = Phone("iPhone", 1000, 1, 1)
    assert phone1.name == "iPhone"
    assert phone1.price == 1000
    assert phone1.quantity == 1
    assert phone1.number_of_sim == 1


def test_phone_number_of_sim_setter():
    phone2 = Phone("Samsung", 900, 2, 2)
    phone2.number_of_sim = 1
    assert phone2.number_of_sim == 1
    with pytest.raises(ValueError):
        phone2.number_of_sim = "2"


def test_keyboard_instantiation():
    keyboard1 = Keyboard("Logitech", 50, 3, "EN")
    assert keyboard1.name == "Logitech"
    assert keyboard1.price == 50
    assert keyboard1.quantity == 3
    assert keyboard1.language == "EN"


def test_keyboard_change_lang():
    keyboard2 = Keyboard("Microsoft", 70, 1, "EN")
    keyboard2.change_lang()
    assert keyboard2.language == "RU"
    keyboard2.change_lang()
    assert keyboard2.language == "EN"

