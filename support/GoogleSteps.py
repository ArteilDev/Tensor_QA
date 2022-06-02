from selenium.webdriver.common.keys import Keys
from support.GooglePage import GooglePage

class GoogleSteps:
    driver = 0

    def __init__(self, webdriver):
        self.driver = webdriver
        self.googlePage = GooglePage()

    def setValueInSearch(self, value):
        searchField = self.googlePage.getInputSearch(self.driver)
        searchField.send_keys(value)
        return searchField
        # searchField.send_keys(Keys.ENTER)

    def getSuggestElement(self):
        suggestElement = self.googlePage.getSuggest(self.driver)
        return suggestElement
    
    def getSearchResult(self):
        searchField = self.googlePage.getInputSearch(self.driver)
        searchField.send_keys(Keys.ENTER) 
        first_link = self.googlePage.getFirstLink(self.driver)
        link_href = first_link.get_attribute('href')
        first_link.click()
        return link_href
