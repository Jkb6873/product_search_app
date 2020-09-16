class Product:
    def __init__(self, id, name, collection, ingredientIds, image):
        self.id = id
        self.name = name
        self.collection = collection
        self.ingredientIds = ingredientIds
        self.image = image

    def __hash__(self):
        return hash(self.id)
