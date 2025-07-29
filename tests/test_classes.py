import pytest
from utils import classes


@pytest.fixture
def product_sapog():
    product = classes.Product('sapog', 'shoe', 12.99, 2)
    try:
        yield product
    finally:
        product._confirm_lower_price = False
        product.priced = 12.99

@pytest.fixture
def product_botinok():
    return classes.Product('botinok', 'another shoe', 17.85, 10)

def test_product(product_sapog, product_botinok):
    assert product_sapog.name == 'sapog'
    assert product_sapog.description == 'shoe'
    assert product_sapog.price == 12.99
    assert product_sapog.availability == 2
    assert product_sapog + product_botinok == 204.48
    assert str(product_sapog) == 'sapog, 12.99 руб. Остаток: 2 шт.'

def test_priced_setter(product_sapog):
    product_sapog.priced = 15.99
    assert product_sapog.priced == 15.99
    product_sapog._confirm_lower_price = True
    product_sapog.priced = 10.99
    product_sapog._confirm_lower_price = False
    with pytest.raises(ValueError):
        product_sapog.priced = -10
    product_sapog._confirm_lower_price = False
    with pytest.raises(TypeError):
        product_sapog.priced = 'string'
    product_sapog._confirm_lower_price = False
    with pytest.raises(ValueError):
        product_sapog.priced = 5.99

@pytest.fixture
def category_obuv(product_sapog, product_botinok):
    x = classes.Category('obuv', 'on your feet')
    x.add_product(product_sapog)
    x.add_product(product_botinok)
    return x

def test_category(category_obuv):
    assert category_obuv.name == 'obuv'
    assert category_obuv.description == 'on your feet'
    assert category_obuv.categories_count == 1
    assert str(category_obuv) == 'obuv - общее количество продуктов: 12'

"""def test_product_reprice(reprice_sapog):
    assert reprice_sapog.out == '11,99'"""
