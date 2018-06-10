from tests.general.selectors_list import SelectorsList
from tests.pages.google_search_results_page import SearchResultsPage

class GoogleHomePage(object):
    
    def __init__(self, selenium_wrapper):
        self.selenium_wrapper = selenium_wrapper
        self.selenium_wrapper.validate_title("Google", "Google home page")
    
    def search_element(self, value):
        self.selenium_wrapper.wait_then_fill_in(SelectorsList.SEARCH_FIELD, value)
        self.selenium_wrapper.wait_and_send_key(SelectorsList.SEARCH_FIELD, "ENTER")
        return SearchResultsPage(self.selenium_wrapper)