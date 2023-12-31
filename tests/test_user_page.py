import pytest
from pages.user_page import UserPage
from pages.add_user_page import AddUserPage
class TestUsersPage():

    def test_open_add_user_page(self,init_driver):
        user_page = UserPage(init_driver)
        user_page.open_url("http://185.67.95.60/users")
        assert user_page.open_add_user_page() == "http://185.67.95.60/add_user"

    def test_get_last_row_data(self, init_driver):
        add_user_page = AddUserPage(init_driver)
        add_user_page.open_url("http://185.67.95.60/add_user")
        add_user_page.create_user('student033@protei.ru','password_22',"Mikailo","Мужской",'1',[1,2])
        user_page = UserPage(init_driver)
        user_page.open_url("http://185.67.95.60/users")
        assert user_page.get_last_row_data() == ['student033@protei.ru',"Mikailo","Мужской",'1.1','2.2']

    def test_table_height_constant(self,init_driver):
        add_user_page = UserPage(init_driver)
        add_user_page.open_url("http://185.67.95.60/users")
        first_time = add_user_page.get_table_height()
        add_user_page.forced_wait(3)
        sec_time = add_user_page.get_table_height()
        assert first_time == sec_time
