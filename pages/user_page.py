import time
from pages.base_page import BasePage
from locators.user_page_locators import UserPageLocators

class UserPage(BasePage):

    def open_add_user_page(self):
        self.do_click(UserPageLocators.add_user_page)
        self.wait_page_load('http://185.67.95.60/add_user')
        return self.get_current_url()


    def get_last_row_data(self):
        el = self.get_group_elements(UserPageLocators.table_rows)
        res = el[-1].text.split()
        return res

    def get_table_height(self):
        style_val = self.get_atr_value(UserPageLocators.table,'style')
        return style_val