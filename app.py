from flask import Flask, request, jsonify, make_response
import requests
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

dummy_json_base_url = 'https://dummyjson.com'

class Welcome(Resource):
    def get(self):
        """
        This is the welcome endpoint of CS 218 API.
        ---
        responses:
          200:
            description: Welcome message
        """

        if 'text/html' in request.headers.get('Accept', '*/*'):
            html_response = make_response("<h1>CS 218 - HW1</h1> <h2>Submitted by: Chinmayi Lokeshwar Hegde (016145025)</h2>")
            html_response.headers['Content-Type'] = 'text/html'
            return html_response
        else:
            return "CS 218 - HW1"

class Products(Resource):
    def get(self):
        """
        This endpoint returns all products.
        ---
        responses:
          200:
            description: List of products
        """
        response = requests.get(f'{dummy_json_base_url}/products')
        return jsonify(response.json())

class ProductCategories(Resource):
    def get(self):
        """
        This endpoint returns all product categories.
        ---
        responses:
          200:
            description: List of product categories
        """
        response = requests.get(f'{dummy_json_base_url}/products/categories')
        return jsonify(response.json())

class SearchProducts(Resource):
    def get(self):
        """
        This endpoint searches for products.
        ---
        parameters:
          - name: q
            in: query
            type: string
            required: true
            description: The search query
        responses:
          200:
            description: List of products matching the search query
        """
        query = request.args.get('q')
        response = requests.get(f'{dummy_json_base_url}/products/search?q={query}')
        return jsonify(response.json())

class SingleProduct(Resource):
    def get(self, product_id):
        """
        This endpoint returns a single product by its ID.
        ---
        parameters:
          - name: product_id
            in: path
            type: string
            required: true
            description: The ID of the product to retrieve
        responses:
          200:
            description: The product details
        """
        response = requests.get(f'{dummy_json_base_url}/products/{product_id}')
        return jsonify(response.json())

api.add_resource(Welcome, '/')
api.add_resource(Products, '/api/products')
api.add_resource(ProductCategories, '/api/products/categories')
api.add_resource(SearchProducts, '/api/products/search')
api.add_resource(SingleProduct, '/api/products/<string:product_id>')

if __name__ == '__main__':
    import os
    if os.environ.get('DOCKER_ENV'):
        app.run(host="0.0.0.0", port=8080, debug=True)
    else:
        app.run(host='localhost', port=8080, debug=True)
