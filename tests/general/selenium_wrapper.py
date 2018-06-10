from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ExpectedConditions

class SeleniumWrapper(object):

    def set_up_web_driver(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.wait = WebDriverWait(self.driver, 12)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def wait_then_fill_in(self, selector, value):
        self.wait.until(
            ExpectedConditions.visibility_of_element_located(selector))
        element = self.driver.find_element(*selector)
        element.click()
        element.send_keys(value)

    def wait_then_click(self, selector):
        self.wait.until(
            ExpectedConditions.visibility_of_element_located(selector))
        self.wait.until(ExpectedConditions.element_to_be_clickable(selector))
        self.driver.find_element(*selector).click()

    def wait_and_send_key(self, selector, key):
        self.wait.until(
            ExpectedConditions.visibility_of_element_located(selector))
        element = self.driver.find_element(*selector)
        element.send_keys(getattr(Keys, key))

    def check_for_duplicates_and_click(self, filter_result_list):
        if(len(filter_result_list) != 0):
            if(len(filter_result_list) == 1):
                filter_result_list[0].click()
            else:
                raise ValueError('Filter results contains duplicate')
        else:
            raise ValueError('Filter results contains no elements')

    def filter_list_by_selector_and_text(self, selector, expected_text):
        elements_list = self.get_driver().find_elements(*selector)
        return list(filter(lambda element: element.text == expected_text, elements_list))

    def check_list_element_with_text_present(self, selector_with_elements, text):
        filter_result_list = self.filter_list_by_selector_and_text(selector_with_elements,
        text)
        
        if(len(filter_result_list) != 0):
            if(len(filter_result_list) == 1):
                return True
            else:
                raise ValueError('Filter results contains duplicate')
        else:
            return False

    def validate_title(self, expected_title, expected_page_name):
        if (self.get_driver().title != expected_title):
            raise ValueError("This is not " + expected_page_name + ", current page is: "
             + self.get_driver().current_url)