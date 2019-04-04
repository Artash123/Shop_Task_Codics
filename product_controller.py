from print_inputs import PrintInputs
from print_statements import PrinterStatemants
from print_lists import PrintLists
from product_manager import ProductManager


class ProductController:

    def add_product(self):
        product = PrintInputs.enter_product()
        product_add = ProductManager().add_product(product)
        if product_add:
            PrinterStatemants.print_product_added()
            return True
        else:
            return False

    def edit_product(self):
        if not PrintLists().print_products(ProductManager().get_product_list()):
            return False
        id = PrintInputs.enter_product_id(ProductManager().get_product_list()[-1].id)
        product = PrintInputs.enter_product()
        product = {'id': id, 'name': product['name'], 'price': product['price'], 'quantity': product['quantity']}
        product_edit = ProductManager().edit_product(product)
        if product_edit:
            PrinterStatemants.print_product_updated()
            return True
        else:
            PrinterStatemants.print_not_found(id, 'product')
            return False

    def remove_product(self):
        if not PrintLists().print_products(ProductManager().get_product_list()):
            return False
        id = PrintInputs.enter_product_id(ProductManager().get_product_list()[-1].id)
        product_remove = ProductManager().remove_product(id)
        if product_remove:
            PrinterStatemants.print_product_removed()
            return True
        else:
            PrinterStatemants.print_not_found(id, 'product')
            return False


