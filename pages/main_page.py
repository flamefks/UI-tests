import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
class MainPage(BasePage):
        # Использовал тайм слип вместо wait_page_load, чтобы в случае возникновения бага, было проще его локализовать
    def open_page_by_click(self,by_locator):
        self.hover_cursor(by_locator)
        self.do_click(by_locator)
        self.forced_wait(1)
        return self.get_current_url()

    def open_page_with_attached_element(self,by_locator):
        self.hover_cursor(MainPageLocators.users_menu)
        self.is_element_visible(by_locator)
        self.do_click(by_locator)
        self.forced_wait(1)
        return self.get_current_url()
