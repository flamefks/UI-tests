from selenium.webdriver.common.by import By
class AuthPageLocators:
    email = (By.CSS_SELECTOR,"#loginEmail")
    password = (By.CSS_SELECTOR,"#loginPassword")
    enter_button = (By.CSS_SELECTOR,"#authButton")
    legend = (By.TAG_NAME,"legend")
    alert_email_passw = (By.CSS_SELECTOR,"#KEKEKEKEKEKKEKE")
    allert_incorrect_email = (By.CSS_SELECTOR,"#emailFormatError")
