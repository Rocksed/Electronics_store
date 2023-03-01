import csv


class Item:
    # class attributes
    price_level = 1  # default is no discount
    products = []
    all = []

    def __init__(self, name, price, quantity):
        # instance attributes
        self._name = name
        self.price = price
        self.quantity = quantity
        # add instance to class attribute
        Item.products.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if int(len(value)) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self._name = value

    def calculate_total_price(self):
        return self.price * self.quantity * Item.price_level

    def apply_discount(self, discount):
        return float(self.price * discount)

    @classmethod
    def instantiate_from_csv(cls):
        with open('../items.csv', encoding='utf8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = Item(name, price, quantity)
                Item.all.append(item)

    @staticmethod
    def is_integer(num):
        if num == int(num):
            return True
        else:
            return False


item = Item('Телефон', 10000, 5)
item.name = 'Смартфон'
print(item.name)

Item.instantiate_from_csv()  # create objects from file data
print(len(Item.all))  # there are 5 items in the file

item1 = Item.all[0]
print(item1.name)

print(Item.is_integer(5))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5))
