import requests
import json
from admin import Admin


class AdminManager:
    def login(self, admin):
        r = requests.post('http://127.0.0.1:8080/login', json=admin)
        response = json.loads(r.text)
        if r.status_code == 200:
            admin = Admin(response['admin']['login'], response['admin']['password'])
            return admin
        return False

    def register(self, admin):
        r = requests.post('http://127.0.0.1:8080/register', json=admin)
        if r.status_code == 200:
            return True
        else:
            return False
