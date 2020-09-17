from .. import db

class Ingredient(db.Model):
    def __init__(self, id, name):
        self.id = id
        self.name = name.title()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    __tablename__ = 'ingredients'
