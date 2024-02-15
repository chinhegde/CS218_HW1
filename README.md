# CS 218 - HW1 

This repository contains the implementation of a REST API developed for CS 218 homework assignment 1. The API utilizes Flask, Flask-Restful, and Flasgger, along with integration of Docker, Pytest for testing, and CI/CD using GitHub Actions.
| Page | Endpoint | Description | 
| -------- | ------- | -------- | 
| Welcome |  `/` | Provides a welcome message for the CS 218 API | 
| Products |  `/api/products` | Returns a list of all products |
| Product Categories |  `/api/products/categories` | Returns a list of all product categories | 
| Search Products |  `/api/products/search` | Searches for products based on a provided query. Parameters: q (query): The search query.
| Single Product |  `/api/products/<product_id>` | Returns details of a single product based on its ID. Parameters: product_id: The ID of the product to retrieve. | 
| Swagger Documentation | `/apidocs/` | Interactive Swagger documentation for all API endpoints. |
