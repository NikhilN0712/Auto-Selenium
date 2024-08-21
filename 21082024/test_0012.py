from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pytest
import allure

@allure.title("Mini Project# 8")
@allure.description("enter capital name ")
@pytest.mark.Mini_Project8
def test_mini_project8():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(2)

    first_name = driver.find_element(By.XPATH,'//input[@name="firstname"]')
    action = ActionChains(driver)
    action.key_down(Keys.SHIFT).send_keys_to_element(first_name,"nikhil").key_up(Keys.SHIFT).perform()
    time.sleep(3)

    driver.quit()

