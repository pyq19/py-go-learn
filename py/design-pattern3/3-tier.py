# coding:utf8
# https://github.com/faif/python-patterns/blob/master/structural/3-tier.py


class Data(object):
    ''' Data Store Class '''

    products = {
        'milk': {'price': 1.50, 'quantity': 10},
        'eggs': {'price': 0.20, 'quantity': 100},
        'cheese': {'price': 2.00, 'quantity': 10}
    }

    def __get__(self, obj, klas):
        print('(Fetching from Data Store)')
        return {'products': self.products}


class BusinessLogic(object):
    ''' Business logic holding data store instances '''
    data = Data()

    def product_list(self):
        return self.data['products'].keys()

    def product_information(self, product):
        return self.data['products'].get(product, None)


class UI(object):
    ''' UI interaction class '''
    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        print('PRODUCT LIST:')
        for product in self.business_logic.product_list():
            print(product)
        print('')

    def get_product_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info:
            print('PRODUCT INFORMATION:')
            print(f"Name: {product.title()} Price: {product_info.get('price', 0)}\
                    Quantity: {product_info.get('quantity', 0)})")
        else:
            print('That product "{product}" does not exist in the records')


def main():
    ui = UI()
    ui.get_product_list()
    ui.get_product_information('cheese')
    ui.get_product_information('eggs')
    ui.get_product_information('milk')
    ui.get_product_information('arepas')


if __name__ == '__main__':
    main()

# PRODUCT LIST:
# (Fetching from Data Store)
# milk
# eggs
# cheese
# 
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Cheese Price: 2.0                    Quantity: 10)
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Eggs Price: 0.2                    Quantity: 100)
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Milk Price: 1.5                    Quantity: 10)
# (Fetching from Data Store)
# That product "{product}" does not exist in the records
