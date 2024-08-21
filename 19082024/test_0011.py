from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import pytest
import allure

@allure.title("Mini Project# 7")
@allure.description("Javascript alert")
@pytest.mark.Mini_Project7
def test_mini_project7():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(2)

    JS = driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]')
    JS.click()
    alert = Alert(driver)
    alert.accept()
    time.sleep(3)

    JS1 = driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]')
    JS1.click()
    alert = Alert(driver)
    alert.dismiss()
    time.sleep(3)

    JS2 = driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]')
    JS2.click()
    alert = Alert(driver)
    alert.send_keys("nikhil")
    alert.accept()
    time.sleep(3)

    driver.quit()

