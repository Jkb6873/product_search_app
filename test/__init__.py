import pytest
import json
import requests
from src import create_app
from src.data import db, ingredient_file, product_file

@pytest.fixture(scope="module", autouse=True)
def setup():
    app = create_app()

    ingredients = requests.get(ingredient_file).json()
    products = requests.get(product_file).json()

    with app.app_context():
        yield {"app":app.test_client(), "db":db, "ingredients":ingredients, "products":products}
        db.drop_all()
