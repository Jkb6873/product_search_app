import pytest
import json
from src import create_app
from src.data import db

@pytest.fixture(scope="module", autouse=True)
def setup():
    app = create_app()

    with open('src/data/ingredients.json') as ingredient_file:
        ingredients = json.load(ingredient_file)
    with open('src/data/products.json') as product_file:
        products = json.load(product_file)

    with app.app_context():
        yield {"app":app.test_client(), "db":db, "ingredients":ingredients, "products":products}
        db.drop_all()
