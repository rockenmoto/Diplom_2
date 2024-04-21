import allure

from data import Data


class TestGetOrders:
    @allure.title('Получение списка заказов авторизированным пользователем')
    def test_get_orders_authorization_user_true(self, user, order):
        user_token = user.login_user(Data.user_email, Data.user_password).json()['accessToken']
        response = order.get_orders(user_token)
        assert (response.status_code == 200 and Data.valid_ingredients in response.text
                and response.json()['orders'] != [])

    @allure.title('Получение списка заказов не авторизированным пользователем')
    def test_get_orders_no_authorization_user_false(self, user, order):
        user_token = ''
        response = order.get_orders(user_token)
        assert (response.status_code == 401 and response.json()['message'] == Data.no_auth_text)
