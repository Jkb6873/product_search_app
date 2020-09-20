from .. import db
from sqlalchemy import PrimaryKeyConstraint

class ProductIngredient(db.Model):
    def __init__(self, product_id, ingredient_id):
        self.product_id = product_id
        self.ingredient_id = ingredient_id

    product_id = db.Column(db.Integer, nullable=False, unique=False)
    ingredient_id = db.Column(db.Integer, nullable=False, unique=False)
    __tablename__ = 'product_ingredients'
    __table_args__ = (PrimaryKeyConstraint(product_id,ingredient_id),{})
