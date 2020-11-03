import json
import os
import requests
from . import db, ingredient_file, product_file
from .models.ingredient import Ingredient
from .models.product import Product
from .models.product_ingredient import ProductIngredient

def populate_db(app):
    with app.app_context():
        db.create_all()
        ingredients = read_ingredients()
        products, product_ingredients = read_products()
        db.session.bulk_save_objects(ingredients)
        db.session.bulk_save_objects(products)
        db.session.bulk_save_objects(product_ingredients)
        db.session.commit()

def read_ingredients():
    ingredient_data = requests.get(ingredient_file).json()
    ingredients = list(map(lambda obj: Ingredient(**obj), ingredient_data))
    return ingredients

def read_products():
    product_data = requests.get(product_file).json()
    product_list = []
    product_ingredients = []
    for product in product_data:
        product_list.append(Product(**product))
        for ingredient_id in product['ingredientIds']:
            product_ingredients.append(ProductIngredient(product['id'], ingredient_id))
    return product_list, product_ingredients
