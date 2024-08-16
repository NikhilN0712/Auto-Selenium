from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@allure.title("Mini Project# 4")
@allure.description("Verify that if user is able to make Appointment")
@pytest.mark.Mini_Project
def test_mini_project4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)

    username = driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")
    login = driver.find_element(By.ID, "btn-login")
    login.click()
    time.sleep(5)

    tet = driver.find_element(By.TAG_NAME,'h2')
    assert tet.text == "Make Appointment"

    driver.quit()


