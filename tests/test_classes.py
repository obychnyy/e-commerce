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


@pytest.fixture
def product_smartphone():
    return classes.Smartphone(50, '15 pro',
                              512, 'black', 'iphone', 'flagman', 100000, 7)


@pytest.fixture
def product_grass():
    return classes.LawnGrass('Greenland', 72, 'juicy green',
                             'some grass', 'the greener than the neighbors',
                             500, 432)


def test_subclasses(product_smartphone, product_grass):
    assert product_smartphone.color == 'black'
    assert product_smartphone.memory == 512
    assert product_smartphone.efficiency == 50
    assert product_smartphone.model == '15 pro'
    assert product_grass.country == 'Greenland'
    assert product_grass.color == 'juicy green'
    assert product_grass.germination_period == 72


def test_summary(product_smartphone, product_grass):
    with pytest.raises(TypeError):
        product_smartphone.__add__(product_smartphone, product_grass)


@pytest.fixture
def category():
    return classes.Category("Тестовая категория", "Описание категории")


class SomeObject:
    pass


def test_add_product_invalid_type(category):
    with pytest.raises(TypeError) as excinfo:
        category.add_product("Это не продукт")
    assert str(excinfo.value) == ("Можно добавлять только объекты "
                                  "класса Product или его подклассов")

    with pytest.raises(TypeError) as excinfo:
        category.add_product(123)
    assert str(excinfo.value) == ("Можно добавлять только объекты "
                                  "класса Product или его подклассов")

    with pytest.raises(TypeError) as excinfo:
        category.add_product([1, 2, 3])
    assert str(excinfo.value) == ("Можно добавлять только объекты "
                                  "класса Product или его подклассов")

    with pytest.raises(TypeError) as excinfo:
        category.add_product({'name': 'test'})
    assert str(excinfo.value) == ("Можно добавлять только объекты "
                                  "класса Product или его подклассов")

    with pytest.raises(TypeError) as excinfo:
        category.add_product(SomeObject())
    assert str(excinfo.value) == ("Можно добавлять только объекты "
                                  "класса Product или его подклассов")
