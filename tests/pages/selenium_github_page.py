from tests.general.selectors_list import SelectorsList

class SeleniumGitHubPage(object):

    def __init__(self, selenium_wrapper):
        expected_title = "GitHub - SeleniumHQ/selenium: A browser automation framework and ecosystem."
        name = "Selenium GitHub page"
        self.selenium_wrapper = selenium_wrapper
        self.selenium_wrapper.validate_title(expected_title, name)

    def is_link_with_text_in_doc_list(self, text):
        selector = SelectorsList.API_DOCUMENTATION_LIST
        driver = self.selenium_wrapper.get_driver()
        driver.get(driver.current_url + "#documentation")
        return self.selenium_wrapper.check_list_element_with_text_present(selector, text)