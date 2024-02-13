from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

dummy_json_base_url = 'https://dummyjson.com'

@app.route('/')
def welcome():
    print("HELLO")

    # if 'text/html' in request.headers.get('Accept', '*/*'):
    return '<h1>Welcome to CS 218!!!</h1>'

    # return 'hello'

@app.route('/api/products', methods=['GET'])
def get_all_products():
    response = requests.get(f'{dummy_json_base_url}/products')
    return jsonify(response.json())

@app.route('/api/products/categories', methods=['GET'])
def get_all_product_categories():
    response = requests.get(f'{dummy_json_base_url}/products/categories')
    return jsonify(response.json())

@app.route('/api/products/search', methods=['GET'])
def search_products():
    query = request.args.get('q')
    response = requests.get(f'{dummy_json_base_url}/products/search?q={query}')
    return jsonify(response.json())

@app.route('/api/products/<product_id>', methods=['GET'])
def get_single_product(product_id):
    print("LINE 35 *****************")
    response = requests.get(f'{dummy_json_base_url}/products/{product_id}')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
