from selenium.webdriver import Chrome


def create_driver():
    driver_chrome = Chrome()
    driver_chrome.maximize_window()
    driver_chrome.get('https://admin-demo.noncommerce.com/')
    yield driver_chrome
    driver_chrome.quit()
