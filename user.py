import allure
import requests

from urls import Urls


class User:
    @allure.step('Регистрация нового пользователя с возвращением списка данных')
    def create_new_user(self, email, password, name):
        login_pass = []
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
            login_pass.append(response.json()['accessToken'])

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
        response = requests.patch(Urls.edit_del_url, headers=headers, data=payload)
        return response

    @allure.step('Удаление пользователя')
    def delete_user(self, user_token):
        headers = {
            'Authorization': user_token,
            'Accept': '*/*'
        }

        requests.delete(Urls.edit_del_url, headers=headers)
