class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.cart = {}
        pass

    def add(self, item):
        if (item.name in self.cart):
            self.cart[item.name] = [self.cart[item.name][0] + 1, self.cart[item.name][1] + item.price]
        else:
            self.cart[item.name] = [1, item.price]

    def total(self):
        count = 0
        for i in self.cart:
            count += i[1]
            print(self.cart[i][1])
        return count

    def __len__(self):
        length = 0
        for i in self.cart:
            length += self.cart[i][0]
        return length

# Making an item...
bike_item = Item('Bike',1000)
banana_item = Item('Banana',1)
print("a bike's item name is... ", bike_item.name)
print("a bike's price is... $", bike_item.price, "(USD)")

# and a shopping cart...
my_cart = ShoppingCart()
# add three bikes
my_cart.add(bike_item)
my_cart.add(bike_item)
my_cart.add(bike_item)
my_cart.add(banana_item)
# check before heading to the register
print(my_cart.cart)
