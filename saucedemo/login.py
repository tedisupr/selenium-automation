import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseLogin
from pageObject.locator import elem
from pageObject.inputan import inputLogin

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_failed_login(self): #test cases 1
        driver = self.browser
        baseLogin.test_failed_login(driver)
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertIn(inputLogin.pesan, error_message)

    def test_success_login(self): #test cases 2
        driver = self.browser
        baseLogin.test_success_login(driver)

if __name__ == '__main__':
    unittest.main()