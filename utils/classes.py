import setter


class Category:
    name: str
    description: str
    products: list
    out: str
    categories_count = 0
    products_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        self.out = ""
        self.categories_count += 1
        self.quantity = 0

    def __str__(self):
        return f'{self.name} - общее количество продуктов: {self.quantity}'

    def add_product(self, NewProduct):
        self.products.append(NewProduct)
        self.products_count = len(self.products)
        self.quantity += NewProduct.availability

"""    @property
    def printered(self):
        for i in self.__products:
            self.out += (f"{i.name}, {i.price}руб. Остаток: {i.availability}шт." + "\n")
        return self.out"""


class Product:
    name: str
    description: str
    price: float
    availability: int
    product_data: dict

    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
        self._confirm_lower_price = False

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.availability} шт.'

    def __add__(self, other):
        return (self.price * self.availability) + (other.price * other.availability)

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)

    @property
    def priced(self):
        return self.price

    @priced.setter
    def priced(self, new_price):
        confirm = ''
        if not isinstance(new_price, (int, float)):
            raise TypeError('Цена должна быть числом')
        if new_price <= 0:
            raise ValueError('Цена должна быть положительной')

        if new_price < self.price:
            if not self._confirm_lower_price:
                raise ValueError("Требуется подтверждение понижения цены")
        self.price = new_price
