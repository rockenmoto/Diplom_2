import allure
import pytest

from data import Data


class TestCreateOrder:

    @allure.title('Создание заказа авторизированным пользователем с валидным ингредиентом')
    def test_create_order_with_login_with_ingredient_true(self, user, order):
        user_token = user.login_user(Data.user_email, Data.user_password).json()['accessToken']
        ingredients = {"ingredients": [f"{Data.valid_ingredients}"]}
        response = order.create_order(ingredients, user_token)
        assert response.status_code == 200 and response.json()['order']['owner']['email'] == Data.user_email

    @allure.title('Создание заказа с авторизацией без и невалидным ингредиентом')
    @pytest.mark.parametrize("ingredient, message, status_code",
                             [[{"ingredients": [f"{Data.fake_ingredients}"]}, Data.fake_ingredient_text, 400],
                              ["", Data.without_ingredient_text, 400]])
    def test_create_order_with_login_without_and_fake_ingredient_false(self, user, order, ingredient, message,
                                                                       status_code):
        user_token = user.login_user(Data.user_email, Data.user_password).json()['accessToken']
        ingredients = ingredient
        response = order.create_order(ingredients, user_token)
        assert response.status_code == status_code and response.json()['message'] == message

    @allure.title('Создание заказа без авторизации с ингредиентом')
    def test_create_order_without_login_with_ingredient_true(self, order):
        user_token = ''
        ingredients = {"ingredients": [f"{Data.valid_ingredients}"]}
        response = order.create_order(ingredients, user_token)
        assert response.status_code == 200 and response.json()['order']['number'] != ''

    @allure.title('Создание заказа без авторизации без и невалидным ингредиентом')
    @pytest.mark.parametrize("ingredient, message, status_code",
                             [[{"ingredients": [f"{Data.fake_ingredients}"]}, Data.fake_ingredient_text, 400],
                              ["", Data.without_ingredient_text, 400]])
    def test_create_order_without_login_with_diff_params_false(self, order, ingredient, message, status_code):
        user_token = ''
        ingredients = ingredient
        response = order.create_order(ingredients, user_token)
        assert response.status_code == status_code and response.json()['message'] == message
