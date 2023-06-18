from selenium.webdriver.common.by import By

class UserPageLocators:
    add_user_page = (By.CSS_SELECTOR,"#addUser")
    table_rows = (By.TAG_NAME,'tr')
    table_emails = (By.TAG_NAME,"td")
    table = (By.CSS_SELECTOR,"#usersPage")