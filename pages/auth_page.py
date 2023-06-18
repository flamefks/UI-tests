from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
from config import ConfigData
class AuthPage(BasePage):

    def do_login(self,email=ConfigData.base_email,password=ConfigData.base_passw):
        self.send_value(AuthPageLocators.email,email)
        self.send_value(AuthPageLocators.password,password)
        self.do_click(AuthPageLocators.enter_button)
        self.forced_wait(1)

    def is_email_or_passw_alert_exist(self,timeout=0):
        self.send_value(AuthPageLocators.email,ConfigData.base_email)
        self.do_click(AuthPageLocators.enter_button)
        self.forced_wait(timeout)
        txt = self.get_el_text(AuthPageLocators.alert_email_passw)
        return txt

    def is_incorrect_email_alert_exist(self,timeout=0):
        self.do_click(AuthPageLocators.enter_button)
        self.forced_wait(timeout)
        return self.get_el_text(AuthPageLocators.allert_incorrect_email)


