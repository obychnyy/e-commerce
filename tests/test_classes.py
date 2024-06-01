import pytest
from utils import classes


@pytest.fixture
def product_sapog():
    return classes.Product('sapog', 'shoe', '12,99', '2')


def test_product(product_sapog):
    assert product_sapog.name == 'sapog'
    assert product_sapog.description == 'shoe'
    assert product_sapog.price == '12,99'
    assert product_sapog.availability == '2'
    assert product_sapog.products_count == 1


@pytest.fixture
def category_obuv():
    return classes.Category('obuv', 'on your feet')


def test_category(category_obuv):
    assert category_obuv.name == 'obuv'
    assert category_obuv.description == 'on your feet'
    assert category_obuv.categories_count == 1


"""@pytest.fixture
def reprice_sapog():
    return classes.Product.set_price(11,99)

def test_product_reprice(reprice_sapog):
    assert reprice_sapog.out == '11,99'"""
