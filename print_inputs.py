from helper_functions import HelperFuncs


class PrintInputs:

    @staticmethod
    def ask_quantity():
        quantity = HelperFuncs().input_int('How many pieces you want? ', 1, 1000)
        return quantity

    def want_to_buy(self, quantity, product_price):
        want_to_buy = input(
            'It will cost {}$, you want it? yes/no '.format(quantity * product_price))
        if want_to_buy in ['yes', 'no']:
            return want_to_buy
        else:
            print('Please type yes or no')
            self.want_to_buy(quantity, product_price)

    @staticmethod
    def print_admin_login():
        print('')
        login = HelperFuncs().check_string("Login: ", 'login', 4, 10)
        password = HelperFuncs().check_string("Password: ", 'password', 4, 10)
        return {'login': login, 'password': password}

    @staticmethod
    def print_admin_register():
        login = HelperFuncs().check_string("Login: ", 'login', 4, 10)
        password = HelperFuncs().check_string("Password: ", 'password', 4, 10)
        return {'login': login, 'password': password}

    @staticmethod
    def enter_product():
        name = HelperFuncs().check_string('Enter product name: ', 'name', 3, 10)
        price = HelperFuncs().input_int('Enter product price: ', 0, 10000)
        quantity = HelperFuncs().input_int('Enter product quantity: ', 0, 1000)
        return {'name': name, 'price': price, 'quantity': quantity}

    @staticmethod
    def enter_product_id(max_id):
        id = HelperFuncs().input_int('Enter product id: ', 1, max_id)
        return int(id)

    @staticmethod
    def enter_worker():
        name = HelperFuncs().check_string('Enter worker name: ', 'name', 3, 10)
        age = HelperFuncs().input_int('Enter worker age: ', 0, 10000)
        salary = HelperFuncs().input_int('Enter worker salary: ', 0, 1000)
        return {'name': name, 'age': age, 'salary': salary}

    @staticmethod
    def enter_worker_id(max_id):
        id = HelperFuncs().input_int('Enter worker id: ', 1, max_id)
        return int(id)

    @staticmethod
    def enter_worker_new_salary():
        salary = HelperFuncs().input_int('Enter worker new salary: ', 1, 1000)
        return int(salary)
