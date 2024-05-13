from selenium import webdriver
from selenium.webdriver.common.by import By
import Hello as hi

hi.hello()
answer = input()
if (answer == 'Да' or answer == 'да' or answer == 'yes' or answer == 'Yes'):
    print('Держи!')
    driver = webdriver.Firefox()
    driver.get('https://ru.wikipedia.org/')
    element = driver.find_element(By.LINK_TEXT, 'Случайная статья')
    element.click()
else:
    print('Ну и иди нахуй')
