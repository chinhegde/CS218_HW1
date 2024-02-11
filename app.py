from bottle import *
import requests
import json

# app = Bottle()

dummy_json_base_url = 'https://dummyjson.com'

@route('/')
def welcome():
    print("HELLO")
    # pprint(dict(request.headers))

    response.set_header('Vary', 'Accept')

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1>Welcome to CS 218!!!</h1>'

    response.content_type = 'text/plain'
    return 'hello'

@route('/api/products', method='GET')
def get_all_products():
    response = requests.get(f'{dummy_json_base_url}/products')
    return response.json()

@route('/api/products/categories', method='GET')
def get_all_product_categories():
    response = requests.get(f'{dummy_json_base_url}/products/categories')
    return response.json()

@route('/api/products/search', method='GET')
def search_products():
    query = request.query.get('q')
    response = requests.get(f'{dummy_json_base_url}/products/search?q={query}')
    return response.json()

@route('/api/products/<product_id>', method='GET')
def get_single_product(product_id):
    response = requests.get(f'{dummy_json_base_url}/products/{product_id}')
    return response.json()

if __name__ == '__main__':
    run(host='localhost', port=8080)
