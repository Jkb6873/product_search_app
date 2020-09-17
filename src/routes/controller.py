import difflib
from . import api
from ..data import db
from ..data.models.ingredient import Ingredient
from ..data.models.product import Product
from ..data.models.product_ingredient import ProductIngredient
from flask import jsonify, request

@api.route('/search', methods=['GET'])
def search():
    ingredient_param = request.args.get("ingredient")
    if not ingredient_param:
        return jsonify({"error": "Request missing valid ingredient parameter"}), 400

    # products = list(db.session.execute("""
    #     select p.name, p.id from products as p
    #     join product_ingredients as pi on (p.id = pi.product_id)
    #     join ingredients as i on (pi.ingredient_id = i.id)
    #     where i.name = '{}'
    # """.format(ingredient_param.title())))

    products = db.session.query(Product)\
                .join(ProductIngredient, Product.id == ProductIngredient.product_id)\
                .join(Ingredient, Ingredient.id == ProductIngredient.ingredient_id)\
                .filter(Ingredient.name == ingredient_param.title())\
                .all()

    if len(products) == 0:
        return jsonify({"error": "No products found containing ingredient '{}'".format(ingredient_param)}), 400

    return jsonify(products), 200
