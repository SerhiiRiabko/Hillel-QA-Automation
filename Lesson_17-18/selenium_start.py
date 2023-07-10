from selenium.webdriver import Chrome


def test_page_title():
    driver_chrome = Chrome()
    driver_chrome.maximize_window()
    driver_chrome.get('http://admin-demo.nopcommerce.com/')

    