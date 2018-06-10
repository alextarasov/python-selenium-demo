import unittest
from general.selenium_wrapper import SeleniumWrapper
from pages.google_home_page import GoogleHomePage

class SearchResultsTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.selenium_wrapper = SeleniumWrapper()
        self.selenium_wrapper.set_up_web_driver()

    def setUp(self):
        self.selenium_wrapper.get_driver().get("https://www.google.com/")
        self.google_home_page = GoogleHomePage(self.selenium_wrapper)

    def test_selenium_page_link_present(self):
        expected_text = "Selenium - Web Browser Automation"
        search_results_page = self.google_home_page.search_element("Selenium")
        result = search_results_page.is_text_present_on_google_page(expected_text)
        self.assertTrue(result, "Link with text '" + expected_text + "' was not found")
        
    def test_github_api_documentation_contain_python(self):
        link_text = "GitHub - SeleniumHQ/selenium: A browser automation framework and ..."
        error_message = "Link with text 'Python' was not found"
        search_results_page = self.google_home_page.search_element("selenium github")
        selenium_github_page = search_results_page.open_selenium_github_page_by_text(link_text)
        self.assertTrue(selenium_github_page.is_link_with_text_in_doc_list("Python"), error_message) 
    
    @classmethod
    def tearDownClass(self):
        self.selenium_wrapper.close()


if __name__ == "__main__":
    unittest.main()
