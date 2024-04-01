import allure
import requests

from urls import Urls


class Order:
    @allure.step('Создание заказа')
    def create_order(self, ingredients, user_token):
        headers = {
            'Authorization': user_token,
            'Accept': '*/*'
        }

        payload = ingredients
        response = requests.post(Urls.orders_url, data=payload, headers=headers)
        return response
