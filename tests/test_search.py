import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from support.Objects import Objects

objects = Objects()

class TestSearch:
    driver = webdriver.Chrome()
    
    def test_search(self):
        self.driver.get('https://www.yandex.ru/')
        
        searchInput = objects.find_element(self.driver, By.XPATH, '//*[@id="text"]')
        objects.setInputValue(searchInput, 'Тензор')
        
        suggest = objects.find_element(self.driver, By.CLASS_NAME, 'mini-suggest__popup_visible')

        objects.setInputValue(searchInput,Keys.ENTER)
        first_link = objects.find_element(self.driver, By.CLASS_NAME, 'serp-item_card a')
        assert first_link.get_attribute('href') ==  "https://tensor.ru/", "Первая ссылка не ведет на tensor.ru"

        self.driver.quit()