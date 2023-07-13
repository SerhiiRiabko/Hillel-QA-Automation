from selenium import webdriver

CHROME = 1
FIREFOX = 2


def create_driver_factory(driver_id):
    if driver_id == CHROME:
        driver = webdriver.Chrome()
