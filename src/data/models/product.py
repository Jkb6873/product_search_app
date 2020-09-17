from .. import db

class Product(db.Model):
    def __init__(self, id, name, collection, **kwargs):
        self.id = id
        self.name = name.title()
        self.collection = collection.title()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    collection = db.Column(db.String(64), unique=False, nullable=True)
    __tablename__ = 'products'
