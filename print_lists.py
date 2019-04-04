from helper_functions import HelperFuncs


class PrintLists:

    @staticmethod
    def print_products(products):
        if len(products) == 0:
            print('No products')
            return False
        for index, product in enumerate(products):
            print('{}.'.format(index + 1), end="  ")
            print('id: {}'.format(product.id), end="  ")
            print('name: {}'.format(product.name), end="  ")
            print('price: {}'.format(product.price), end=" ")
            print('quantity: {}'.format(product.quantity), end="  ")
            print('')
        return True

    @staticmethod
    def print_products_paginate(products, page, last_page):
        print('')
        if len(products) == 0:
            print('Oops, shop is empty')
            return False
        print('Item ID  Name        Price     Quantity')
        print('___________________________________________')
        for index, product in enumerate(products):
            print('{}.'.format(index + 1), end=" ")
            print((6 - len(str(index + 1))) * ' ', end=" ")
            if len(product.name) > 8:
                print('{}..'.format(product.name[0:8]), end=" ")
                print('  ', end=" ")
            else:
                print(product.name, end=" ")
                print((12 - len(product.name)) * ' ', end=" ")
            print('{}$'.format(product.price), end=" ")
            print((7 - len(str(product.price))) * ' ', end=" ")
            print('{} pieces'.format(product.quantity), end=" ")
            print('')
        print('_______________')
        if not page == 1:
            print('8. Previous', end="   ")
        if not page == last_page:
            print('9. Back', end="   ")
            print('10. Next')
        else:
            print('9. Back')
        index = HelperFuncs().input_int('What you want to buy? ', 1, 10)
        return index

    @staticmethod
    def print_workers(workers):
        if len(workers) == 0:
            print('No workers')
            return False
        for index, worker in enumerate(workers):
            print('{}.'.format(index+1), end = " ")
            print('id: {}'.format(worker.id), end=" ")
            print('name: {}'.format(worker.name), end=" ")
            print('age: {}'.format(worker.age), end=" ")
            print('salary: {}'.format(worker.salary), end=" ")
            print('')
        return True
