import setter


class Category:
    name: str
    description: str
    products: list
    out: str
    categories_count = 0
    products_count = 0
    quantity = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        self.out = ""
        Category.categories_count += 1

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.quantity}'

    def add_product(self, NewProduct):
        self.__products.append(NewProduct)
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

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.availability}'

    def __add__(self, other):
        return (self.price * self.availability) + (other.price * other.availability)

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        confirm = ""
        if price > 0:
            if self.price > price:
                print("Вы действительно хотите понизить цену?")
                print("y/n")
                confirm = input()
                if confirm == 'y':
                    self.price = price
            else:
                self.price = price
        else:
            print('Вы уверены, что это цена?')
