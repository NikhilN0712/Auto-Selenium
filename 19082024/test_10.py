from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@allure.title("Mini Project# 6")
@allure.description("check the checkbox")
@pytest.mark.Mini_Project6
def test_mini_project6():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(2)

    chek1 = driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]')
    chek1.click()
    time.sleep(2)

    chek2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    chek2.click()
    time.sleep(2)

    chek3 = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
    chek3[1].click()
    time.sleep(2)

    driver.quit()
    

