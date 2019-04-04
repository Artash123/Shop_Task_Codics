from print_menu import PrintMenu
from print_lists import PrintLists
from print_statements import PrinterStatemants
from product_controller import ProductController
from worker_controller import WorkerController
from accountancy import Accountancy
from admin_controller import AdminController
from buyer import Buyer
product_controller = ProductController()
worker_controller = WorkerController()
admin_controller = AdminController()


def start_shop():
    sel_main_menu = PrintMenu.print_main_menu()
    if sel_main_menu == 1:
        if not Buyer().choose_product(1):
            start_shop()
    if sel_main_menu == 2:
        if admin_controller.login():
            choose_admin_action()
        else:
            start_shop()
    if sel_main_menu == 3:
        exit()


def choose_admin_action():
    sel = PrintMenu.print_admin_menu()
    if int(sel) == 1:
        show_accountancy()
    if int(sel) == 2:
        change_products()
    if int(sel) == 3:
        change_staff()
    if int(sel) == 4:
        if admin_controller.register():
            choose_admin_action()
        choose_admin_action()
    if int(sel) == 5:
        start_shop()


def show_accountancy():
    sel = PrintMenu().print_accountancy_menu()
    if int(sel) == 1:
        product_list = Accountancy().get_sold_products()
        PrintLists().print_products(product_list)
        show_accountancy()
    if int(sel) == 2:
        profit = Accountancy().get_profit()
        PrinterStatemants().print_profit(profit)
        show_accountancy()
    if int(sel) == 3:
        profit = Accountancy().get_total_salary()
        PrinterStatemants().print_total_salary(profit)
        show_accountancy()
    if int(sel) == 4:
        choose_admin_action()
    if int(sel) == 5:
        start_shop()


def change_products():
    sel = PrintMenu().print_product_edit_menu()
    if int(sel) == 1:
        product_controller.add_product()
        change_products()
    if int(sel) == 2:
        product_controller.edit_product()
        change_products()
    if int(sel) == 3:
        product_controller.remove_product()
        change_products()
    if int(sel) == 4:
        choose_admin_action()
    if int(sel) == 5:
        start_shop()


def change_staff():
    sel = PrintMenu().print_workers_edit_menu()
    if int(sel) == 1:
        worker_controller.add_worker()
        change_staff()
    if int(sel) == 2:
        worker_controller.edit_worker_salary()
        change_staff()
    if int(sel) == 3:
        worker_controller.lay_off_worker()
        change_staff()
    if int(sel) == 4:
        choose_admin_action()
    if int(sel) == 5:
        start_shop()


start_shop()
