import time
from locators.add_user_page_locators import AddUserPageLocators
from pages.base_page import BasePage
from typing import Union
class AddUserPage(BasePage):

    def create_user(self,email,password,name,text,r_button:Union[str,int],check_box:Union[str,int,list,tuple,set, None]):
        self.send_value(AddUserPageLocators.email,email)
        self.send_value(AddUserPageLocators.password,password)
        self.send_value(AddUserPageLocators.name,name)
        self.select_option(AddUserPageLocators.gender,text)
        choice_r_button = (AddUserPageLocators.radio_button[0], AddUserPageLocators.radio_button[1] + str(r_button))
        self.do_click(choice_r_button)
        if type(check_box) in [str,int]:
            choice_check_box = ( AddUserPageLocators.check_box[0], AddUserPageLocators.check_box[1] + str(check_box))
            self.do_click(choice_check_box)
            print(choice_check_box)
        elif type(check_box) in [list,tuple,set]:
            check_box = [i for i in set(check_box)]
            for i in range(len(check_box)):
                choice_check_box = (AddUserPageLocators.check_box[0], AddUserPageLocators.check_box[1] + str(check_box[i]))
                self.do_click(choice_check_box)
                print(choice_check_box)
        else:
            pass
        self.do_click(AddUserPageLocators.confirm_button)
        return self.bin_is_element_visible(AddUserPageLocators.user_added)