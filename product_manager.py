import requests
import json
from product import Product


class ProductManager:

    def get_product_list(self, page=None):
        products = []
        if page:
            page = str(page)
            r = requests.get('http://127.0.0.1:8080/products/'+page)
            if r.status_code == 200:
                response = json.loads(r.text)
                product_dict = response['products']
                for product in product_dict:
                    product = Product(product['id'], product['name'], product['price'], product['quantity'])
                    products.append(product)
                return {'products': products, 'last_page': response['last_page']}
        else:
            r = requests.get('http://127.0.0.1:8080/products')
            response = json.loads(r.text)
            if r.status_code == 200:
                response = response['products']
                for product in response:
                    product = Product(product['id'], product['name'], product['price'], product['quantity'])
                    products.append(product)
                return products
        return False

    def add_product(self, product):
        r = requests.post('http://127.0.0.1:8080/product', json=product)
        if r.status_code == 200:
            return True
        else:
            return False

    def edit_product(self, product):
        if int(product['quantity']) == 0:
            self.remove_product(product.id)
            return True
        r = requests.put('http://127.0.0.1:8080/product', json=product)
        if r.status_code == 200:
            return True
        else:
            return False

    def remove_product(self, id):
        id = int(id)
        r = requests.delete('http://127.0.0.1:8080/product', json=id)
        if r.status_code == 200:
            return True
        else:
            return False

    def get_product(self, id):
        id = str(id)
        r = requests.get('http://127.0.0.1:8080/product/'+id)
        response = json.loads(r.text)
        if r.status_code == 200:
            product = response['product']
            product = Product(product['id'], product['name'], product['price'], product['quantity'])
            return product
        else:
            return False