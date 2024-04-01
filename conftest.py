import pytest
from user import User
from order import Order


@pytest.fixture(scope='function')
def user():
    user = User()
    return user


@pytest.fixture(scope='function')
def user_data(user):
    user_data = user.create_new_user()
    return user_data


@pytest.fixture(scope='function')
def order():
    order = Order()
    return order
