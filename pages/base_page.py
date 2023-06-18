import time
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support.ui import Select
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        # self.url = url

    # Переход по url
    def open_url(self,url):
        self.driver.get(url)

    def is_element_visible(self,by_locator):
        return Wait(self.driver,timeout=2).until(Ec.visibility_of_element_located(by_locator))

    def bin_is_element_visible(self,by_locator):
        try:
            (Wait(self.driver,timeout=2).until(Ec.visibility_of_element_located(by_locator)))
        except Exception:
            return False
        return True
    # Несколько элементов
    def get_group_elements(self,by_locator):
        return Wait(self.driver,timeout=2).until(Ec.visibility_of_all_elements_located(by_locator))
        # return self.driver.find_elements(By.TAG_NAME,"tr")

    # Клик
    def do_click(self,by_locator):
        Wait(self.driver,timeout=2).until(Ec.visibility_of_element_located(by_locator)).click()

    # Отправить значение в поле ввода
    def send_value(self,by_locator,message):
        Wait(self.driver,timeout=2).until(Ec.visibility_of_element_located(by_locator)).send_keys(message)

    # Узнать текущий url
    def get_current_url(self):
        return self.driver.current_url

    # Получить текст элемента
    def get_el_text(self,by_locator):
        el = Wait(self.driver,timeout=2).until(Ec.visibility_of_element_located(by_locator))
        return el.text

    # Ожидание загрузки страницы
    def wait_page_load(self,url):
        Wait(self.driver,timeout=2).until(Ec.url_matches(url))

    def select_option(self,by_locator,text=""):
        element = self.is_element_visible(by_locator)
        selection_el = Select(element)
        selection_el.select_by_visible_text(text)

    def forced_wait(self,timeout):
        time.sleep(timeout)

    def hover_cursor(self,by_locator):
        # element = Wait(self.driver,timeout=5).until(Ec.visibility_of_element_located(by_locator))
        element = self.is_element_visible(by_locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def get_atr_value(self,by_locator,atr_name):
        element = self.is_element_visible(by_locator)
        return element.get_attribute(atr_name)