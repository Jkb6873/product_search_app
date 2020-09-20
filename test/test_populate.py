import os
import json
import pytest
from src.data.models.product import Product
from src.data.models.ingredient import Ingredient
from src.data.models.product_ingredient import ProductIngredient
from . import setup

def test_db_row_count_matches_json(setup):
    db = setup['db']
    products = setup['products']
    ingredients = setup['ingredients']

    product_ingredient_count = sum(map(lambda obj: len(obj['ingredientIds']), products))
    assert db.session.query(Product).count() == len(products)
    assert db.session.query(Ingredient).count() == len(ingredients)
    assert db.session.query(ProductIngredient).count() == product_ingredient_count

def test_names_with_non_standard_characters_unmodified(setup):
    db = setup['db']
    products = setup['products']
    json_product = list(filter(lambda obj: obj['id'] == 48, products))[0]

    db_product = db.session.query(Product).filter(Product.id == json_product['id']).first()
    assert json_product['name'] == db_product.name

def test_urls_unmodified(setup):
    db = setup['db']
    json_product = setup['products'][0]

    db_product = db.session.query(Product).filter(Product.id == json_product['id']).first()
    assert json_product['image']['url'] == db_product.img_url

def test_ingredientids_mapped_to_product_ingredients(setup):
    db = setup['db']
    json_product = setup['products'][0]

    db_product = db.session.query(Product).filter(Product.id == json_product['id']).first()
    db_product_ingredients = list(map(lambda obj: obj[0], db.session.query(ProductIngredient.ingredient_id)\
                                .filter(ProductIngredient.product_id == db_product.id).all()))
    assert json_product['collection'] == db_product.collection
    assert set(json_product['ingredientIds']) == set(db_product_ingredients)
    assert len(json_product['ingredientIds']) == len(db_product_ingredients)
