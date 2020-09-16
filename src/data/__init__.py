import json
from models.ingredient import Ingredient
from models.product import Product

#read products.json into a dictionary of id -> Product
with open('products.json') as product_file:
    products = dict(map(lambda obj: (obj['id'], Product(**obj)), json.load(product_file)))
#read ingredients.json into a dictionary of id -> Ingredient
with open('ingredients.json') as ingredient_file:
    ingredients = dict(map(lambda obj: (obj['id'], Ingredient(**obj)), json.load(ingredient_file)))

#map each ingredient to all products that contain that ingredient
ingredient_to_product_map = {}
for (p_id, product) in products.items():
    for ingredient_id in product.ingredientIds:
        if ingredients[ingredient_id] in ingredient_to_product_map:
            ingredient_to_product_map[ingredients[ingredient_id]].add(product)
        else:
            ingredient_to_product_map[ingredients[ingredient_id]] = set([product])
