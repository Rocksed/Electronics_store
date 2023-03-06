import csv


class Item:
    # class attributes
    price_level = 1  # default is no discount
    products = []
    all = []

    def __init__(self, name, price, quantity):
        # attributes instance
        self._name = name
        self.price = price
        self.quantity = quantity
        # add instance to class attribute
        self.__class__.products.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if int(len(value)) > 10:
            raise Exception("The length of the product name exceeds 10 characters.")
        else:
            self._name = value

    def calculate_total_price(self):
        return self.price * self.quantity * self.__class__.price_level

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
                cls.all.append(item)

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


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name


class Inventory:
    def __init__(self):
        self.stock = {}

    def add_item(self, item):
        if isinstance(item, Item):
            self.stock[item] = self.stock.get(item, 0) + 1
        else:
            raise TypeError("Only instances of Item class can be added to the inventory.")

    def add_phone(self, phone):
        if isinstance(phone, Phone):
            self.stock[phone] = self.stock.get(phone, 0) + 1
        else:
            raise TypeError("Only instances of Phone class can be added to the inventory.")


phone1 = Phone("iPhone 14", 120_000, 5, 2)
print(phone1)

print(repr(phone1))
Phone('iPhone 14', 120000, 5, 2)
phone1.number_of_sim = 0
