import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.title("Mini Project# 14")
@allure.description("Verify that if user is able to make Appointment")
@pytest.mark.Mini_Project
def test_project():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    clk = driver.find_element(By.ID, "btn-make-appointment")
    clk.click()

    time.sleep(2)

    use = driver.find_element(By.ID, "txt-username")
    use.send_keys("John Doe")
    ps = driver.find_element(By.ID, "txt-password")
    ps.send_keys("ThisIsNotAPassword")

    bto = driver.find_element(By.ID, "btn-login")
    bto.click()

    time.sleep(2)

    Facility = driver.find_element(By.ID, "combo_facility")
    select = Select(Facility)
    select.select_by_visible_text("Hongkong CURA Healthcare Center")

    time.sleep(2)

    che_box = driver.find_element(By.ID, "chk_hospotal_readmission")
    che_box.click()

    time.sleep(2)

    redio = driver.find_element(By.ID, "radio_program_medicaid")
    redio.click()

    time.sleep(2)

    date = driver.find_element(By.ID, "txt_visit_date")
    date.send_keys("02/10/2024")

    time.sleep(2)

    com = driver.find_element(By.ID, "txt_comment")
    com.send_keys("Hello Dr")

    time.sleep(2)

    sub = driver.find_element(By.ID, "btn-book-appointment")
    sub.submit()

    time.sleep(5)

    txt = driver.find_element(By.TAG_NAME,"h2")
    assert txt.text == "Appointment Confirmation"

    allure.attach(driver.get_screenshot_as_png(), name='appointment_Screenshot')
    driver.quit()
