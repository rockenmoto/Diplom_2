import allure
import pytest
import requests
from data import Data
from urls import Urls
from generator import Generator


class TestCreateUser:

    @allure.title('Проверяем успешное создание пользователя c обязательными полями')
    def test_create_user_true(self, user, user_data):
        assert len(user_data) == 5

    @allure.title('Проверяем создание 2 пользователей с одинаковыми данными')
    def test_create_two_same_users_false(self, user, user_data):
        email = user_data[0]
        password = user_data[1]
        name = user_data[2]

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(Urls.register_url, data=payload)
        assert (response.status_code == 403 and
                response.json()['message'] == Data.login_already_use_error_text)

    @allure.title('Проверка создания пользователя без обязательного поля')
    @pytest.mark.parametrize("field_one, field_two",
                             [["email", "name"],
                              ["password", "email"],
                              ["password", "name"]
                              ])
    def test_create_user_without_required_false(self, field_one, field_two):
        field_one_data = Generator.generate_random_string(5)
        field_two_data = Generator.generate_random_string(5)

        payload = {
            f"{field_one}": field_one_data,
            f"{field_two}": field_two_data
        }

        response = requests.post(Urls.register_url, data=payload)
        assert (response.status_code == 403 and
                response.json()['message'] == Data.not_enough_data_error_text)
