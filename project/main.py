import csv
import os


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
        Item.products.append(self)

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
        return self.price * self.quantity * Item.price_level

    def apply_discount(self, discount):
        return float(self.price * discount)

    @classmethod
    def instantiate_from_fcsv(cls):
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

    def __add__(self, other):
        if isinstance(other, Item):
            new_item = Item(self.name, self.price, self.quantity + other.quantity)
            return new_item
        elif isinstance(other, Phone):
            new_phone = Phone(self.name, self.price, self.quantity + other.quantity, self.number_of_sim)
            return new_phone
        else:
            raise TypeError("Cannot add instances of different classes.")


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not Item.is_integer(value) or int(value) <= 0:
            raise ValueError("Number of physical SIM cards must be integer greater than zero.")
        else:
            self._number_of_sim = int(value)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


class LanguageAddOn:
    def __init__(self, language='EN'):
        self._language = language

    @property
    def language(self):
        return self._language

    def change_lang(self):
        self._language = 'RU' if self._language == 'EN' else 'EN'


class Keyboard(Item, LanguageAddOn):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        LanguageAddOn.__init__(self, language)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, '{self.language}')"

    def __str__(self):
        return self.name


kb = Keyboard('Dark Project KD87A', 9600, 5)
print(kb)
print(kb.language)
kb.change_lang()
print(kb.language)
#kb.language = 'CH'
