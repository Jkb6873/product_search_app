class Ingredient:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __hash__(self):
        return hash(self.id)
