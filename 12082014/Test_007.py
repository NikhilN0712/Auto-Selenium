from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@allure.title("Mini Project# 3")
@allure.description("Verify that if user validity is expired and needs to upgrade")
@pytest.mark.Mini_Project
def test_mini_project3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.idrive360.com/enterprise/login')
    email = driver.find_element(By.ID,'username')
    email.send_keys("augtest_040823@idrive.com")
    pw = driver.find_element(By.ID,'password')
    pw.send_keys("123456")
    btn = driver.find_element(By.ID,'frm-btn')
    btn.click()

    time.sleep(20)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    upg = driver.find_element(By.XPATH,"//button[@class='id-btn id-warning-btn-drk id-tkn-btn']")
    print(upg.text)
    time.sleep(5)
    assert upg.text == 'Upgrade Now!'

    driver.close()


