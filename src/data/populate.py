import json
import os
from . import db
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
    data_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(data_dir, 'ingredients.json')) as ingredient_file:
        ingredients = list(map(lambda obj: Ingredient(**obj), json.load(ingredient_file)))
    return ingredients

def read_products():
    data_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(data_dir, 'products.json')) as product_file:
        product_data = json.load(product_file)
        product_list = []
        product_ingredients = []
        for product in product_data:
            product_list.append(Product(**product))
            for ingredient_id in product['ingredientIds']:
                product_ingredients.append(ProductIngredient(product['id'], ingredient_id))
    return product_list, product_ingredients
