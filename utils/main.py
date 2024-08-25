from classes import Category, Product

"""iphone15 = Product('iphone 15', 'can call and take a photo', '1499,99', '17')
iphone15pro = Product('iphone 15 pro', 'can call and take a photo, but better', '1899,99', '11')"""

iphone15 = input()

new_prod_1 = Product.new_product(iphone15)

iphone15pro = input()

new_prod_2 = Product.new_product(iphone15pro)

phones = Category('phones', 'for calls')

Category.add_product(phones, iphone15)
Category.add_product(phones, iphone15pro)
phones.printered()