from selenium import webdriver
from selenium.webdriver.common.by import By
import platform
import logging


def randomwiki():
    browser = find_default_browser()
    driver_class = getattr(webdriver, browser)
    driver = driver_class()
    driver.get('https://ru.wikipedia.org/')
    element = driver.find_element(By.LINK_TEXT, 'Случайная статья')
    element.click()
    isClosed = False
    while isClosed == False:
        try:
            driver.title
        except RuntimeError:
            isClosed = True


def find_default_browser():
    osPlatform = platform.system()

    if osPlatform == 'Windows':

        try:
            from winreg import HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, OpenKey, QueryValueEx

            with OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice') as regkey:
                browser_choice = QueryValueEx(regkey, 'ProgId')[0]

        except Exception:
            logging.error('Failed to look up default browser')

    if browser_choice[0] == 'C':
        browser_choice = browser_choice.split('HTML')[0]
    elif browser_choice[0] == 'F':
        browser_choice = browser_choice.split('URL')[0]
    elif browser_choice[0] == 'M':
        browser_choice = browser_choice[2:6]

    return browser_choice