class Product:
    def __init__(self, name, price, quantity, id=None):
        self.id = id  # Añadido para manejar el ID autoincremental de MySQL
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):  # Nombre más genérico (no específico de MongoDB)
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

    @classmethod
    def from_dict(cls, data):  # Nuevo método útil para MySQL
        return cls(
            id=data.get('id'),
            name=data['name'],
            price=data['price'],
            quantity=data['quantity']
        )