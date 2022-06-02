from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Objects:


    def setInputValue(self, object, value):
        return object.send_keys(value)
    
    
    def find_element(self, driver, locator, object):
        return WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((locator, object)),'Объект: '+object+' не обнаружен!')
    
    
    def find_elements(self, driver, locator, object):
        return WebDriverWait(driver, 5, 0.5).until(EC.presence_of_all_elements_located((locator, object)),'Объекты: '+object+' не обнаружен!')
