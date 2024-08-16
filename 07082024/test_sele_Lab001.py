from selenium import webdriver
import allure



def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"
