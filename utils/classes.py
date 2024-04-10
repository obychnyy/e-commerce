class Category:
    name: str
    description: str
    products: list
    categories_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.categories_count += 1


class Product:
    name: str
    description: str
    price: float
    availability: int
    products_count = 0

    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
        Product.products_count += 1
