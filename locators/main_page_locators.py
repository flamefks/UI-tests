from selenium.webdriver.common.by import By
class MainPageLocators:
    auth_page = (By.CSS_SELECTOR,"#menuAuth")
    main_page = (By.CSS_SELECTOR,"#menuMain")
    users_menu = (By.ID,"menuUsersOpener")
    users_page = (By.CSS_SELECTOR,"#menuUsers")
    add_user_page = (By.CSS_SELECTOR,"#menuUserAdd")
    more_page = (By.CSS_SELECTOR,"#menuMore")
