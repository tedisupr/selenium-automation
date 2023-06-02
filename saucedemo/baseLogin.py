import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.locator import elem
from pageObject.inputan import inputLogin

def test_failed_login(driver): #test cases 1
    driver.implicitly_wait(10)
    driver.get(inputLogin.baseUrl)
    driver.find_element(By.ID, elem.username).send_keys(inputLogin.userInvalid)
    driver.find_element(By.NAME, elem.loginButton).click()

def test_success_login(driver): #test cases 2
    driver.get(inputLogin.baseUrl)
    driver.find_element(By.ID, elem.username).send_keys(inputLogin.userValid)
    driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputLogin.password)
    driver.find_element(By.NAME, elem.loginButton).click()

