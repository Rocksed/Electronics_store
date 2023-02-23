class Item:
    # class attributes
    price_level = 1  # default is no discount
    products = []

    def __init__(self, name, price, quantity):
        # instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity
        # add instance to class attribute
        Item.products.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity * Item.price_level

    def apply_discount(self, discount):
        return float(self.price * discount)


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

# set a new price level
print(item1.apply_discount(0.8))
print(item2.price)

print(Item.products)
