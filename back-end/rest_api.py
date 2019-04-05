from flask import Flask, jsonify, request
import json
app = Flask(__name__)
admin_filename = 'admins.json'
product_filename = 'products.json'
soldproduct_filename = 'sold_products.json'
workers_filename = 'workers.json'


@app.route('/login',methods=['POST'])
def login():
    data = request.get_json(force=True)
    login = data['login']
    password = data['password']
    with open(admin_filename) as json_data:
        admin_list = json.load(json_data)
    if admin_list:
        for admin in admin_list:
            if admin['login'] == login and admin['password'] == password:
                return jsonify({'admin': {'login': admin['login'], 'password': admin['password']}}),200
    return jsonify({'message':'not found'}),404


@app.route('/register',methods=['POST'])
def register():
    data = request.get_json(force=True)
    login = data['login']
    password = data['password']
    with open(admin_filename) as json_data:
        admin_list = json.load(json_data)
    for admin in admin_list:
        if login == admin['login']:
            return jsonify({'massage': 'login already exist'}), 404
    last_id = 0
    if len(admin_list):
        last_id = admin_list[-1]['id']+1
    admin = {'id':last_id,'login':login,'password':password}
    admin_list.append(admin)
    data = admin_list
    with open(admin_filename, 'w') as outfile:
        json.dump(data, outfile)
    return jsonify({'success': 1}), 200


@app.route('/products',methods=['GET'])
def get_products():
    with open(product_filename) as json_data:
        product_list = json.load(json_data)
    return jsonify({'products': product_list}),200


@app.route('/product/<id>',methods=['GET'])
def get_product(id):
    id = int(id)
    with open(product_filename) as json_data:
        product_list = json.load(json_data)
    for index, product in enumerate(product_list):
        if product['id'] == id:
            return jsonify({'product': product}),200
    return jsonify({'message': 'not found'}),404


@app.route('/products/<page>',methods=['GET'])
def get_product_paginate(page):
    products_in_page = 5
    page = int(page)
    start = (page-1)*products_in_page
    end = (page)*products_in_page
    with open(product_filename) as json_data:
        product_list = json.load(json_data)
    last_page = int(len(product_list)/products_in_page)+1
    return jsonify({'products': product_list[start:end],'last_page': last_page}),200


@app.route('/product',methods=['POST'])
def add_product():
    data = request.get_json(force=True)
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    with open(product_filename) as json_data:
        product_list = json.load(json_data)
    last_id = 1
    if len(product_list):
        last_id = product_list[-1]['id']+1
    product = {'id':last_id,'name':name,'price':price, 'quantity':quantity}
    product_list.append(product)
    data = product_list
    with open(product_filename, 'w') as outfile:
        json.dump(data, outfile)
    return jsonify({'message': 'success'}),200


@app.route('/product',methods=['PUT'])
def edit_product():
    data = request.get_json(force=True)
    id = data['id']
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    with open(product_filename) as json_data:
        product_list = json.load(json_data)
    for index, product in enumerate(product_list):
        if product['id'] == id:
            product_list[index] = {'id': id, 'name': name, 'price': price, 'quantity': quantity}
            data = product_list
            with open(product_filename, 'w') as outfile:
                json.dump(data, outfile)
            return jsonify({'product': product_list[index]}),200
    return jsonify({'message': 'not found'}),404


@app.route('/product',methods=['DELETE'])
def delete_product():
    data = request.get_json(force=True)
    id = int(data)
    with open(product_filename) as json_data:
        product_list = json.load(json_data)
    for index, product in enumerate(product_list):
        if product['id'] == id:
            del product_list[index]
            data = product_list
            with open(product_filename, 'w') as outfile:
                json.dump(data, outfile)
            return jsonify({'message': 'success'}), 200
    return jsonify({'message': 'not found'}), 404


@app.route('/worker',methods=['GET'])
def get_workers():
    with open(workers_filename) as json_data:
        workers_list = json.load(json_data)
    return jsonify({'workers': workers_list}), 200


@app.route('/worker',methods=['POST'])
def add_worker():
    data = request.get_json(force=True)
    name = data['name']
    age = data['age']
    salary = data['salary']
    with open(workers_filename) as json_data:
        workers_list = json.load(json_data)
    last_id = 1
    if len(workers_list):
        last_id = workers_list[-1]['id']+1
    worker = {'id': last_id, 'name': name, 'age': age, 'salary': salary}
    workers_list.append(worker)
    data = workers_list
    with open(workers_filename, 'w') as outfile:
        json.dump(data, outfile)
    return jsonify({'message': 'success'}), 200


@app.route('/worker',methods=['PUT'])
def edit_worker_salary():
    data = request.get_json(force=True)
    id = data['id']
    salary = data['salary']
    with open(workers_filename) as json_data:
        workers_list = json.load(json_data)
    for index, worker in enumerate(workers_list):
        if worker['id'] == id:
            workers_list[index] = {'id': id, 'name': worker['name'], 'age': worker['age'], 'salary': salary}
            data = workers_list
            with open(workers_filename, 'w') as outfile:
                json.dump(data, outfile)
            return jsonify({'worker': workers_list[index]}), 200
    return jsonify({'message': 'not found'}), 404


@app.route('/worker',methods=['DELETE'])
def delete_worker():
    data = request.get_json(force=True)
    id = int(data)
    with open(workers_filename) as json_data:
        workers_list = json.load(json_data)
    for index, worker in enumerate(workers_list):
        if worker['id'] == id:
            del workers_list[index]
            data = workers_list
            with open(workers_filename, 'w') as outfile:
                json.dump(data, outfile)
            return jsonify({'message': 'success'}), 200
    return jsonify({'message': 'not found'}), 404


@app.route('/soldProduct',methods=['POST'])
def add_sold_product():
    data = request.get_json(force=True)
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    with open(soldproduct_filename) as json_data:
        product_list = json.load(json_data)
    last_id = 0
    if len(product_list):
        last_id = product_list[-1]['id']+1
    product = {'id':last_id,'name':name,'price':price, 'quantity':quantity}
    product_list.append(product)
    data = product_list
    with open(soldproduct_filename, 'w') as outfile:
        json.dump(data, outfile)
    return jsonify({'message': 'success'}),200


@app.route('/soldProduct',methods=['GET'])
def get_sold_product():
    with open(soldproduct_filename) as json_data:
        product_list = json.load(json_data)
    return jsonify({'products': product_list}),200


if __name__ == '__main__':
    app.run(debug=True,port=8080)

