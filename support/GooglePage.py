from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage:


    def getInputSearch(self,driver):
        inputSearch = self.ec_find(driver, By.XPATH, '//*[@id="text"]')
        return inputSearch

    def getSuggest(self, driver):
        suggest = self.ec_find(driver, By.CLASS_NAME, 'mini-suggest__popup_visible')
        return suggest
    
    def getFirstLink(self, driver):
        first_link = self.ec_find(driver, By.CLASS_NAME, 'serp-item_card a')
        return first_link
    
    def ec_find(self, driver, locator, element):
        return WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((locator, element)),'Not enought: '+element)
