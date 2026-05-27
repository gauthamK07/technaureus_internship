class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price


class Cart:

    def __init__(self):

        self.items = []

    def add_product(self, product):

        self.items.append(product)

    def total_price(self):

        total = 0

        for item in self.items:

            total += item.price

        return total


class Order:

    def __init__(self, cart):

        self.cart = cart

    def final_price(self, discount):

        total = self.cart.total_price()

        final = total - (total * discount / 100)

        return final


p1 = Product("Laptop", 50000)

p2 = Product("Mouse", 1000)

cart = Cart()

cart.add_product(p1)

cart.add_product(p2)

order = Order(cart)

print("Total =", cart.total_price())

print("Final Price =", order.final_price(10))