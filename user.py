import random
import string

import allure
import requests

from urls import Urls


class User:
    response = None

    @allure.step('Регистрация нового пользователя с возвращением списка данных')
    def create_new_user(self):
        login_pass = []

        # генерируем логин, пароль и имя курьера
        email = self.generate_random_string(15) + "@yandex.ru"
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        self.response = requests.post(Urls.register_url, data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if self.response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)
            login_pass.append(name)
            login_pass.append(self.response.json()['accessToken'])
            login_pass.append(self.response.json()['refreshToken'])

        # возвращаем список
        return login_pass

    @allure.step('Логин пользователя')
    def login_user(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Urls.login_url, data=payload)
        return response

    @allure.step('Генерация строки')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string
