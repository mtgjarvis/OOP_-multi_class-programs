from product import Product

class ShoppingCart:
    '''
    Totals the cost of items added to shopping cart and allows for items to be added and removed
    '''

    def __init__(self, shopping_cart = []):
        self.shopping_cart = shopping_cart


    def add_to_cart(self, new_item):
        self.shopping_cart.append(new_item)

    def remove_from_cart(self, item_index):
        self.shopping_cart.pop(item_index)   

    def before_tax(self):
        total_before_tax = 0
        for item in self.shopping_cart:
            total_before_tax += item.base_price 
        return total_before_tax

    def after_tax(self):
        total = 0
        for item in self.shopping_cart:
            total += item.total_price_item()
        return total

    def display_cart(self,):
        print('Your Cart has: ')
        for item in self.shopping_cart:
            print(item)

newcart = ShoppingCart()

newcart.add_to_cart(Product('Avacado', 0.99, .10))
newcart.add_to_cart(Product('Orange', 1.19, 0))
newcart.add_to_cart(Product('Colgate', 3.99,))
newcart.add_to_cart(Product('Blueberries', 3.99, 0))
newcart.add_to_cart(Product('Charmen', 8.99))

newcart.display_cart()
print(newcart.before_tax())
print(newcart.after_tax())

newcart.remove_from_cart(1)

newcart.display_cart()
print(newcart.before_tax())
print(newcart.after_tax())

