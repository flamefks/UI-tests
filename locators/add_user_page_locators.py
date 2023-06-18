from selenium.webdriver.common.by import By
class AddUserPageLocators:
    email = (By.CSS_SELECTOR,"#dataEmail")
    password = (By.CSS_SELECTOR,"#dataPassword")
    name = (By.CSS_SELECTOR,"#dataName")
    gender = (By.CSS_SELECTOR,"#dataGender")
    radio_button = (By.CSS_SELECTOR,"#dataSelect1")
    check_box = (By.CSS_SELECTOR,"#dataSelect2")
    confirm_button = (By.CSS_SELECTOR,"#dataSend")
    user_added = (By.CLASS_NAME,"uk-modal-body")
