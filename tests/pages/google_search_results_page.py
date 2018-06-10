from tests.general.selectors_list import SelectorsList
from tests.pages.selenium_github_page import SeleniumGitHubPage

class SearchResultsPage(object):

    def __init__(self, selenium_wrapper):
        self.selenium_wrapper = selenium_wrapper

    def is_text_present_on_google_page(self, text):
        return self.selenium_wrapper.check_list_element_with_text_present(SelectorsList.SEARCH_RESULTS,
        text)
    
    def open_selenium_github_page_by_text(self, text_to_find):
        filter_result_list = self.selenium_wrapper.filter_list_by_selector_and_text(SelectorsList.SEARCH_RESULTS,
        text_to_find)
        self.selenium_wrapper.check_for_duplicates_and_click(filter_result_list)
        return SeleniumGitHubPage(self.selenium_wrapper)