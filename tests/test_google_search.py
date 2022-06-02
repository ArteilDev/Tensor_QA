import pytest
import time
from selenium import webdriver
from support.GoogleSteps import GoogleSteps

def test_search():
    
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.yandex.ru/")
    tester = GoogleSteps(driver)
    tester.setValueInSearch("Тензор")
    suggest = tester.getSuggestElement()
    assert suggest != True, "Таблица с подсказками не обнаружена!"
    searchResult = tester.getSearchResult()
    print("Первая ссылка ведет на: "+ searchResult)
    if searchResult == "https://tensor.ru/":
        tensor = True
    else:
        tensor = False
    print(tensor)
    assert tensor != True, "Error"


if __name__ == '__main__':
    pytest.main(["-s -v", "test_google_search.py"])