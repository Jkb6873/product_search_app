from .. import db

class Product(db.Model):
    def __init__(self, id, name, collection, image, ingredientIds, **kwargs):
        self.id = id
        self.name = name.title()        #.title() enforces a standard, not 100% necessary
        self.collection = collection.title()
        self.ingredient_ids = ingredientIds
        self.img_url = image['url'] if image else None

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    collection = db.Column(db.String(64), unique=False, nullable=True)
    ingredient_ids = db.Column(db.JSON(), unique=False, nullable=True) #double stored since we have product_ingredient table, but faster retrieval
    img_url = db.Column(db.Text(), unique=False, nullable=True)   #text is more variable in length.
    __tablename__ = 'products'
