import pytest
from pages.auth_page import AuthPage
from config import ConfigData
class TestAuthPage:
    # Т.к. пароль и email мы создаем на странице /add_users, то и валидация значений (наличие домена и тд) должна быть там
    # здесь же проверяем валидность (существует пользователь/не существует)

    @pytest.mark.parametrize('email, password, res',[(ConfigData.base_email,ConfigData.base_passw,True),
                                                     ('student@protei.ru','student22',False),
                                                     ('student@protei.ru','student',True),
                                                     ('test@ protei.ru',ConfigData.base_passw,False),
                                                     ('','',False)])
    def test_do_login(self,init_driver,email,password,res):
        auth_page = AuthPage(init_driver)
        auth_page.open_url("http://185.67.95.60")
        auth_page.do_login(email,password)
        ans =  auth_page.get_current_url() != "http://185.67.95.60/"
        assert ans == res

    # Проверка появления и удержания алерта о неверном формате email
    @pytest.mark.parametrize('timeout',[(0),
                                        (1)])
    def test_incorrect_email_alert_exist(self,init_driver,timeout):
        auth_page = AuthPage(init_driver)
        auth_page.open_url("http://185.67.95.60")
        assert auth_page.is_incorrect_email_alert_exist(timeout) == "Неверный формат E-Mail" # alert appear

    # Проверка появления и удержания алерта о неверно введенных email или password
    @pytest.mark.parametrize('timeout',[(0),
                                        (1)])
    def test_email_or_passw_alert_exist(self,init_driver,timeout):
        auth_page = AuthPage(init_driver)
        auth_page.open_url("http://185.67.95.60")
        assert auth_page.is_email_or_passw_alert_exist(timeout) == "Неверный E-Mail или пароль" # alert appear

