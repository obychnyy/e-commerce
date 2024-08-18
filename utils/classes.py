import setter


class Category:
    name: str
    description: str
    products: list
    out: str
    categories_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        self.out = ""
        Category.categories_count += 1


    def add_product(self, NewProduct):
        self.__products.append(NewProduct)


    def printered(self):
        for i in self.__products:
            self.out += (f"{i.name}, {i.price}руб. Остаток: {i.availability}шт." + "\n")
        return self.out


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

    def make_new_product(self, info):
        print('Введите название товара')
        {}['name'] = input()


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

