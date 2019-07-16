class Product:
    '''
    Products for purchase
    '''

    def __str__(self):
        return (f'{self.name}, {self.base_price}, {self.tax_rate}')

    def __init__(self, name, base_price, tax_rate = []):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def total_price_item(self):
        total_price_item = self.base_price * self.tax_rate + self.base_price
        return total_price_item
