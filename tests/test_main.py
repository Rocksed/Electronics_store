import pytest
from project.main import Item, Phone, Inventory


@pytest.fixture
def inventory():
    return Inventory()


def test_add_items(inventory):
    item1 = Item("item1", 100, 5)
    item2 = Item("item2", 200, 3)
    inventory.add_item(item1)

