import pytest

from generator import Generator
from user import User
from order import Order


@pytest.fixture(scope='function')
def user():
    user = User()
    return user


@pytest.fixture(scope='function')
def user_data(user):
    email = Generator.generate_rdm_str(5) + "@yandex.ru"
    password = Generator.generate_rdm_str(5)
    name = "User_" + Generator.generate_rdm_str(5)

    user_data = user.create_new_user(email, password, name)
    yield user_data

    user.delete_user(user_data[3])


@pytest.fixture(scope='function')
def order():
    order = Order()
    return order
