import allure
import pytest

from data import Data
from generator import Generator


class TestEditUser:
    @allure.title('Проверка изменения пользовательских данных авторизованным пользователем')
    @pytest.mark.parametrize("new_email, new_pass, new_name",
                             [[Generator.generate_rdm_str(5) + "@yandex.ru", Generator.generate_rdm_str(5),
                               "User_" + Generator.generate_rdm_str(5)],
                              ['jqjlk@yandex.ru', "User_" + Generator.generate_rdm_str(5),
                               Generator.generate_rdm_str(5)]
                              ])
    def test_edit_data_for_auth_user(self, user, new_email, new_pass, new_name):
        valid_email = 'jqjlk@yandex.ru'
        valid_pass = 'fpzzx'
        valid_name = 'User_fxiju'

        user_token = user.login_user(valid_email, valid_pass).json()['accessToken']

        edited_response = user.edit_data_user(new_email, new_pass, new_name, user_token)
        edited_email = edited_response.json()['user']['email']
        edited_name = edited_response.json()['user']['name']

        login_response = user.login_user(edited_email, new_pass)
        assert (edited_response.status_code == 200 and edited_email == new_email
                and edited_name == new_name and login_response.status_code == 200)

        user.edit_data_user(valid_email, valid_pass, valid_name, user_token)

    @allure.title('Проверка изменения пользовательских данных не авторизованным пользователем')
    def test_edit_data_for_no_auth_user(self, user):
        user_token = ''

        new_email = Generator.generate_rdm_str(5) + "@yandex.ru"
        new_name = "User_" + Generator.generate_rdm_str(5)
        new_pass = Generator.generate_rdm_str(5)

        response = user.edit_data_user(new_email, new_pass, new_name, user_token)
        assert response.status_code == 401 and response.json()['message'] == Data.no_auth_text
