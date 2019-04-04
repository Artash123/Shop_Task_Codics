from worker_manager import WorkerManager
from product import Product
import json
import requests


class Accountancy:

    def __init__(self):
        self.sold_products = []
        self.profit = 0

    def get_total_salary(self):
        total_salary = 0
        workers = WorkerManager().get_worker_list()
        for worker in workers:
            total_salary += worker.salary
        return total_salary

    def get_sold_products(self):
        r = requests.get('http://127.0.0.1:8080/soldProduct')
        response = json.loads(r.text)
        if r.status_code == 200:
            product_dict = response['products']
            for product in product_dict:
                product = Product(product['id'], product['name'], product['price'], product['quantity'])
                self.sold_products.append(product)
            return self.sold_products
        else:
            return False

    def add_sold_product(self,product):
        product = product.__dict__
        r = requests.post('http://127.0.0.1:8080/soldProduct', json=product)
        if r.status_code == 200:
            return True
        else:
            return False

    def get_profit(self):
        products = self.get_sold_products()
        if len(products) > 0:
            for product in products:
                self.profit += product.price*product.quantity
        return self.profit

