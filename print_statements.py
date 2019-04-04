class PrinterStatemants:

    @staticmethod
    def print_thanks_purchase():
        print('')
        print('Thank you for your purchase')

    @staticmethod
    def print_not_found(id, item):
        print("There is no {} with id: {}".format(item,id))

    @staticmethod
    def print_no_so_much():
        print("We don't have that much")

    @staticmethod
    def print_product_added():
        print('')
        print('Product added')

    @staticmethod
    def print_product_updated():
        print('')
        print('Product updated')

    @staticmethod
    def print_product_removed():
        print('')
        print('Product removed')

    @staticmethod
    def print_worker_added():
        print('')
        print('Worker accepted')

    @staticmethod
    def print_worker_salary_updated():
        print('')
        print('Worker salary updated')

    @staticmethod
    def print_worker_fired():
        print('')
        print('Worker fired')

    @staticmethod
    def print_profit(profit):
        print('Your profit is {}$'.format(profit))

    @staticmethod
    def print_total_salary(total_salary):
        print('Total salary of your workers is {}$'.format(total_salary))

    @staticmethod
    def print_greet_admin(login):
        print('')
        print('Hi {}'.format(login))

    @staticmethod
    def print_wrong_login():
        print('Wrong login or password')

    @staticmethod
    def print_register_success():
        print('Admin registered successful')

    @staticmethod
    def print_register_error():
        print('This login is already exist')



