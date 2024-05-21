from selenium import webdriver
from selenium.webdriver.common.by import By

def randomwiki():
    driver = webdriver.Firefox()
    driver.get('https://ru.wikipedia.org/')
    element = driver.find_element(By.LINK_TEXT, 'Случайная статья')
    element.click()