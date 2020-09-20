import pytest
from src import create_app
from . import setup

def test_search_matches_format(setup):
    client = setup['app']

    res = client.get('/search', query_string = {"ingredient": "Watermelon"})
    product = res.json[0]
    assert "id" in product
    assert "name" in product
    assert "collection" in product
    assert "image" in product
    assert "ingredientIds" in product
    assert "url" in product["image"]
    assert len(product.items()) == 5


def test_search_returns_all_products(setup):
    client = setup['app']

    res = client.get('/search', query_string = {"ingredient": "Oregano"})
    assert len(res.json) == 2
    res = client.get('/search', query_string = {"ingredient": "Watermelon"})
    assert len(res.json) == 1
    res = client.get('/search', query_string = {"ingredient": "Organic Raspberry"})
    assert len(res.json) == 5

def test_search_no_ingredient_param(setup):
    client = setup['app']

    res = client.get('/search')
    assert res.status_code == 400
    assert res.json == {"error": "Request missing valid ingredient parameter"}

def test_search_ingredient_not_found(setup):
    client = setup['app']

    res = client.get('/search', query_string = {"ingredient": "eggs"})
    assert res.status_code == 400
    assert res.json == {"error": "No products found containing ingredient 'eggs'"}

def test_search_case_matching(setup):
    client = setup['app']

    res1 = client.get('/search', query_string = {"ingredient": "Oregano"})
    res2 = client.get('/search', query_string = {"ingredient": "OrEgAnO"})
    res3 = client.get('/search', query_string = {"ingredient": "oregano"})
    res4 = client.get('/search', query_string = {"ingredient": "OREGANO"})

    assert res1.json == res2.json == res3.json == res4.json
