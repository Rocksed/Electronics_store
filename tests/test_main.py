import pytest
from project.main import Item, Phone, Keyboard, LanguageAddOn, InstantiateCSVError
import csv


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


@pytest.fixture
def item():
    return Item('test', 1.0, 1)


def test_instantiate_from_csv_success(self, tmp_path):
    # Create a temporary csv file with data
    csv_data = "name,price,quantity\nitem1,10.0,5\nitem2,20.0,3\n"
    csv_file = tmp_path / "items.csv"
    csv_file.write_text(csv_data)

    # Instantiate items from the csv file
    items = Item.instantiate_from_csv(str(csv_file))

    # Check that the items are instantiated correctly
    assert len(items) == 2
    assert items[0].name == "item1"
    assert items[0].price == 10.0
    assert items[0].quantity == 5
    assert items[1].name == "item2"
    assert items[1].price == 20.0
    assert items[1].quantity == 3


def test_instantiate_from_csv_error(self, tmp_path):
    # Create a temporary csv file with invalid data
    csv_data = "name,price,quantity\nitem1,10.0,5\nitem2,20.0,invalid\n"
    csv_file = tmp_path / "items.csv"
    csv_file.write_text(csv_data)

    # Check that the InstantiateCSVError is raised when invalid data is encountered
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(str(csv_file))


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


class TestKeyboard:
    def test_initialization(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert kb.name == 'Dark Project KD87A'
        assert kb.price == 9600
        assert kb.quantity == 5
        assert kb.language == 'EN'

    def test_change_language(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert kb.language == 'EN'
        kb.change_lang()
        assert kb.language == 'RU'
        kb.change_lang()
        assert kb.language == 'EN'

    def test_string_representation(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert str(kb) == 'Dark Project KD87A'

    def test_repr_representation(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5, 'EN')"

    def test_inheritance(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert isinstance(kb, Keyboard)
        assert isinstance(kb, Item)
        assert isinstance(kb, LanguageAddOn)
