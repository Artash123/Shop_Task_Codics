from print_inputs import PrintInputs
from print_statements import PrinterStatemants
from admin_manager import AdminManager


class AdminController:
    def __init__(self):
        self.admin = None
        if AdminController.__instance:
            raise Exception("This class is a singleton!")
        else:
            AdminController.__instance = self

    def login(self):
        if self.admin:
            return True
        admin = PrintInputs.print_admin_login()
        login = AdminManager().login(admin)
        if login:
            self.admin = login
            PrinterStatemants.print_greet_admin(self.admin.login)
            return True
        else:
            PrinterStatemants.print_wrong_login()
            return False

    @staticmethod
    def register():
        admin = PrintInputs.print_admin_register()
        register = AdminManager().register(admin)
        if register:
            PrinterStatemants.print_register_success()
            return True
        else:
            PrinterStatemants.print_register_error()
            return False

    __instance = None

    @staticmethod
    def get_instance():
        if not AdminController.__instance:
            AdminController()
        return AdminController.__instance
