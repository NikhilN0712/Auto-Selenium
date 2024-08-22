from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import allure

@allure.title("Mini Project# 13")
@allure.description("Calculate the Total Amount of Money Spent via Selenium Script")
@pytest.mark.Mini_Project13
def test_mini_project13():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.applitools.com/")
    time.sleep(2)

    id = driver.find_element(By.ID,"username")
    id.send_keys("admin")

    pwd = driver.find_element(By.ID,"password")
    pwd.send_keys("password@12")

    sub = driver.find_element(By.ID,"log-in")
    sub.click()

    time.sleep(5)

    table = driver.find_element(By.XPATH,'//table[@class="table table-padded"]')

    rows = table.find_elements(By.TAG_NAME, 'tr')

    total_amount_spent = 0.0
    for row in rows[1:]:  # Skip the header row if present
        amount_cell = row.find_elements(By.TAG_NAME, 'td')[4]
        amount_text = amount_cell.text
        if amount_text.startswith('+'): # Remove the '+' sign and convert to float
           amount = float(amount_text.replace('+', '').replace('-', '').replace(',', '').replace('USD',''))  # Remove currency symbol and commas
           total_amount_spent += amount
        elif amount_text.startswith('-'): #If amount has a '-' sign or no sign, it is ignored
            continue

    print(f"Total Amount Spent: {total_amount_spent:.2f}")

    driver.quit()



