from selenium.webdriver.common.by import By

class SelectorsList(object):
    SEARCH_FIELD = (By.XPATH, "//input[@type='text']")
    SEARCH_RESULTS = (By.XPATH, "//div//*[@class='r']//a")
    API_DOCUMENTATION_LIST = (By.XPATH, "//*[@id='readme']/article/ul[2]/li/a") 