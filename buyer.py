from product_manager import ProductManager
from print_inputs import PrintInputs
from print_lists import PrintLists
from accountancy import Accountancy
from print_statements import PrinterStatemants
product_manager = ProductManager()


class Buyer:

    def choose_product(self, page):
        products_paginate = product_manager.get_product_list(page)
        products = products_paginate['products']
        last_page = products_paginate['last_page']
        index = PrintLists.print_products_paginate(products, page, last_page)
        if len(products) == 0:
            return False
        if (page-1) >= 1:
            if index == 8:
                if not self.choose_product(page - 1):
                    return False
        if index == 9:
            return False
        if not page == last_page:
            if index == 10:
                if not self.choose_product(page + 1):
                    return False
        if len(products) < index:
            PrinterStatemants().print_not_found(index, 'product')
            return self.choose_product(page)
        quantity = PrintInputs.ask_quantity()
        product_price = product_manager.get_product_list(page)['products'][index-1].price
        if PrintInputs().is_want_to_buy(quantity, product_price) == 'yes':
            if self.buy_product(index, page, quantity):
                PrinterStatemants().print_thanks_purchase()
        self.choose_product(page)

    def buy_product(self, index, page, quantity):
        current_product = product_manager.get_product_list(page)['products'][index - 1]
        current_id = current_product.id
        if not product_manager.get_product(current_id):
            PrinterStatemants().print_not_found(current_id, 'product')
            return False
        if current_product.quantity < quantity:
            PrinterStatemants().print_no_so_much()
            return False
        current_quantity = current_product.quantity - quantity
        current_product.quantity = current_quantity
        sold_product = product_manager.get_product(current_id)
        sold_product.quantity = quantity
        Accountancy().add_sold_product(sold_product)
        current_product = current_product.__dict__
        if product_manager.edit_product(current_product):
            return True
