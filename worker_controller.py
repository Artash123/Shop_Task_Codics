from print_inputs import PrintInputs
from print_lists import PrintLists
from print_statements import PrinterStatemants
from worker_manager import WorkerManager


class WorkerController:
    def __init__(self):
        self.workers = []

    def add_worker(self):
        worker = PrintInputs.enter_worker()
        if worker['age'] <= 18:
            print("We can't take him, he is too young")
            return False
        if worker['age'] >= 65:
            print("We can't take a pensioner")
            return False
        worker_add = WorkerManager().add_worker(worker)
        if worker_add:
            PrinterStatemants.print_worker_added()
            return True
        else:
            return False

    def edit_worker_salary(self):
        if not PrintLists().print_workers(WorkerManager().get_worker_list()):
            return False
        id = PrintInputs.enter_worker_id(WorkerManager().get_worker_list()[-1].id)
        salary = PrintInputs.enter_worker_new_salary()
        worker_edit = WorkerManager().edit_worker_salary(id, salary)
        if worker_edit:
            PrinterStatemants.print_worker_salary_updated()
            return True
        else:
            PrinterStatemants.print_not_found(id, 'worker')
            return False

    def lay_off_worker(self):
        if not PrintLists().print_workers(WorkerManager().get_worker_list()):
            return False
        id = PrintInputs.enter_worker_id(WorkerManager().get_worker_list()[-1].id)
        worker_remove = WorkerManager().remove_worker(id)
        if worker_remove:
            PrinterStatemants.print_worker_fired()
            return True
        else:
            PrinterStatemants.print_not_found(id, 'worker')
            return False

