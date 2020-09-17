from flask import json
from data.models.ingredient import Ingredient
from data.models.product import Product

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return {
                'id': obj.id,
                'name': obj.name,
                'collection': obj.collection,
            }
        if isinstance(obj, Ingredient):
            return {
                'id': obj.id,
                'name': obj.name
            }
        return super(CustomEncoder, self).default(obj)
