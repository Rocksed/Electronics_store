import pytest
from project.main import Item, Phone


def test_name_length_limit():
    with pytest.raises(Exception):
        item = Item("This name is too long", 10, 1)


def test_calculate_total_price():
    item = Item("Book", 5, 3)
    assert item.calculate_total_price() == 15
    Item.price_level = 0.8
    assert item.calculate_total_price() == 12


def test_apply_discount():
    item = Item("Book", 5, 1)
    assert item.apply_discount(0.2) == 1.0


def test_instantiate_from_fcsv():
    Item.instantiate_from_fcsv()
    assert len(Item.all) == 3
    assert Item.all[0].name == "Book"
    assert Item.all[1].name == "Pen"
    assert Item.all[2].name == "Pencil"


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.1) == False


def test_add_items():
    item1 = Item("Book", 5, 2)
    item2 = Item("Pen", 1, 4)
    assert (item1 + item2).quantity == 6
    with pytest.raises(TypeError):
        phone = Phone("iPhone 14", 120_000, 1, 1)
        item1 + phone


def test_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 1, 2)
    assert phone.number_of_sim == 2
    with pytest.raises(ValueError):
        phone.number_of_sim = "not a number"
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
