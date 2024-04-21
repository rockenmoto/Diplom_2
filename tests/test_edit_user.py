import allure

from data import Data
from generator import Generator


class TestEditUser:
    @allure.title('Проверка изменения пользовательских данных на новые авторизованным пользователем')
    def test_edit_data_with_new_values_for_auth_user_true(self, user, user_data):
        new_email = Generator.generate_rdm_str(5) + "@yandex.ru"
        new_pass = Generator.generate_rdm_str(5)
        new_name = "User_" + Generator.generate_rdm_str(5)

        user_token = user.login_user(user_data[0], user_data[1]).json()['accessToken']
        edited_response = user.edit_data_user(new_email, new_pass, new_name, user_token)

        edited_email = edited_response.json()['user']['email']
        edited_name = edited_response.json()['user']['name']

        login_response = user.login_user(edited_email, new_pass)
        assert (edited_response.status_code == 200 and edited_email == new_email
                and edited_name == new_name and login_response.status_code == 200)

    @allure.title('Проверка изменения пользовательских данных c актуальной почтой авторизованным пользователем')
    def test_edit_data_with_same_email_for_auth_user_false(self, user, user_data):
        same_email = Data.same_email
        new_pass = Generator.generate_rdm_str(5)
        new_name = "User_" + Generator.generate_rdm_str(5)

        user_token = user.login_user(user_data[0], user_data[1]).json()['accessToken']
        edited_response = user.edit_data_user(same_email, new_pass, new_name, user_token)
        assert edited_response.status_code == 403 and edited_response.json()['message'] == Data.email_exists_text

    @allure.title('Проверка изменения пользовательских данных не авторизованным пользователем')
    def test_edit_data_for_no_auth_user_false(self, user):
        user_token = ''

        new_email = Generator.generate_rdm_str(5) + "@yandex.ru"
        new_name = "User_" + Generator.generate_rdm_str(5)
        new_pass = Generator.generate_rdm_str(5)

        response = user.edit_data_user(new_email, new_pass, new_name, user_token)
        assert response.status_code == 401 and response.json()['message'] == Data.no_auth_text
