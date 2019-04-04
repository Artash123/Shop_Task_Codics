from helper_functions import HelperFuncs


class PrintMenu:

    @staticmethod
    def print_main_menu():
        print('')
        print('1. Go to shopping')
        print('2. Admin')
        print('3. Quit')
        print('_______________')
        sel = HelperFuncs().input_int('Select what you want: ', 1, 3)
        return sel

    @staticmethod
    def print_admin_menu():
        print('')
        print('1. Accountancy')
        print('2. Edit Products')
        print('3. Edit Staff')
        print('4. Add Admin')
        print('5. Back')
        print('_______________')
        sel = HelperFuncs().input_int('Choose an action: ', 1, 5)
        return sel

    @staticmethod
    def print_product_edit_menu():
        print('')
        print('1. Add product')
        print('2. Edit product')
        print('3. Remove product')
        print('4. Back')
        print('5. Home')
        print('_______________')
        sel = HelperFuncs().input_int('What do you want to do? ', 1, 5)
        print('')
        return sel

    @staticmethod
    def print_workers_edit_menu():
        print('')
        print('1. Add worker')
        print('2. Edit worker salary')
        print('3. Lay off worker')
        print('4. Back')
        print('5. Home')
        print('_______________')
        sel = HelperFuncs().input_int('What do you want to do? ', 1, 5)
        return sel

    @staticmethod
    def print_accountancy_menu():
        print('')
        print('1. Show sold products')
        print('2. Show profit')
        print('3. Show tatal salary')
        print('4. Back')
        print('5. Home')
        print('_______________')
        sel = HelperFuncs().input_int('what do you want to see? ', 1, 5)
        return sel
