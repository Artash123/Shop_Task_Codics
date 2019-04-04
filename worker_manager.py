import requests
import json
from worker import Worker


class WorkerManager:

    def get_worker_list(self):
        workers = []
        r = requests.get('http://127.0.0.1:8080/worker')
        if r.status_code == 404:
            exit()
        response = json.loads(r.text)
        if r.status_code == 200:
            response = response['workers']
            for worker in response:
                worker = Worker(worker['id'], worker['name'], worker['age'], worker['salary'])
                workers.append(worker)
            return workers
        return False

    def add_worker(self, worker):
        r = requests.post('http://127.0.0.1:8080/worker', json=worker)
        if r.status_code == 200:
            return True
        else:
            return False

    def edit_worker_salary(self, id, salary):
        data = {'id': id, 'salary':salary}
        r = requests.put('http://127.0.0.1:8080/worker', json=data)
        if r.status_code == 200:
            return True
        else:
            return False

    def remove_worker(self, id):
        id = int(id)
        r = requests.delete('http://127.0.0.1:8080/worker', json=id)
        if r.status_code == 200:
            return True
        else:
            return False


