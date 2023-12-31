import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
class TestMainPage:
    @pytest.mark.parametrize('locator,res',[(MainPageLocators.auth_page,"http://185.67.95.60/auth"),
                                            (MainPageLocators.main_page,"http://185.67.95.60/main"),
                                            (MainPageLocators.more_page,"http://185.67.95.60/more"),
                                            (MainPageLocators.users_menu, "http://185.67.95.60/users")
                                            ])
    def test_open_page_by_click(self,init_driver,locator,res):
        main_page = MainPage(init_driver)
        main_page.open_url("http://185.67.95.60/main")
        assert main_page.open_page_by_click(locator) == res

    @pytest.mark.parametrize('locator,res',[(MainPageLocators.users_page,"http://185.67.95.60/users"),
                                            (MainPageLocators.add_user_page,"http://185.67.95.60/add_user")])
    def test_open_page_with_attached_element(self,init_driver,locator,res):
        main_page = MainPage(init_driver)
        main_page.open_url("http://185.67.95.60/main")
        assert main_page.open_page_with_attached_element(locator) ==res



