import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import ConfigData
@pytest.fixture()
def init_driver():
    service = Service(ConfigData.driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()