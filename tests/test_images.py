import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from support.Objects import Objects

objects = Objects()

class TestImage:
    driver = webdriver.Chrome()
    
    def test_image(self):
        self.driver.get('https://yandex.ru')
        
        image_link = objects.find_element(self.driver, By.XPATH, '//a[@href="https://yandex.ru/images/?utm_source=main_stripe_big"]')
        image_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        first_category = objects.find_element(self.driver, By.CLASS_NAME, 'PopularRequestList-Item_pos_0 .PopularRequestList-SearchText')
        category = first_category.text
        first_category.click()

        input_img = objects.find_element(self.driver, By.CLASS_NAME, 'mini-suggest__input')
        input_img_text = input_img.get_attribute('value')
        assert category == input_img_text, 'Неверное название категории'
        
        first_image = objects.find_element(self.driver, By.CLASS_NAME, 'serp-item_pos_0')
        first_image.click()
        
        image = objects.find_element(self.driver, By.CLASS_NAME, 'MMImageContainer img')
        image_src = [image.get_attribute('src')]
        
        next_button = objects.find_element(self.driver, By.CLASS_NAME, 'MediaViewer-LayoutScene .CircleButton_type_next')
        next_button.click()
        
        image = objects.find_element(self.driver, By.CLASS_NAME, 'MMImageContainer img')
        image_src.append(image.get_attribute('src'))
        assert image_src[0] != image_src[1], 'Картинка не сменилась'
        
        prev_button = objects.find_element(self.driver, By.CLASS_NAME, 'MediaViewer-LayoutScene .CircleButton_type_prev')
        prev_button.click()
        assert image_src[1] != image_src[0], 'Картинка не сменилась'

        self.driver.quit()
        
        