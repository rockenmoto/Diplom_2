import allure
import requests

from urls import Urls
from generator import Generator


class User:
    @allure.step('Регистрация нового пользователя с возвращением списка данных')
    def create_new_user(self):
        login_pass = []

        email = Generator.generate_rdm_str(5) + "@yandex.ru"
        password = Generator.generate_rdm_str(5)
        name = "User_" + Generator.generate_rdm_str(5)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(Urls.register_url, data=payload)

        if response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)
            login_pass.append(name)

        return login_pass

    @allure.step('Логин пользователя')
    def login_user(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Urls.login_url, data=payload)
        return response

    @allure.step('Изменения данных пользователя')
    def edit_data_user(self, email, password, name, user_token):
        headers = {
            'Authorization': user_token,
            'Accept': '*/*'
        }

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.patch(Urls.edit_user_data_url, headers=headers, data=payload)
        return response
