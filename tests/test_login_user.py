import allure
import pytest

from data import Data


class TestLoginUser:
    @allure.title('Проверка авторизации пользователя с обязательными полями')
    def test_login_user_true(self, user):
        response = user.login_user(Data.user_email, Data.user_password)
        assert response.status_code == 200

    @allure.title('Проверка авторизации с неверным логином или паролем')
    @pytest.mark.parametrize("email, password",
                             [[Data.user_email, "fake_password"],
                              ["fake_email", Data.user_password],
                              ["fake_email", "fake_password"]
                              ])
    def test_login_user_with_incorrect_data_false(self, user, email, password):
        response = user.login_user(email, password)
        assert response.status_code == 401 and response.json()['message'] == Data.account_not_found_error_text
