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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name


item1 = Item("Смартфон", 10000, 20)
Item('Смартфон', 10000, 20)
print(item1)
