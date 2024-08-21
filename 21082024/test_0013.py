from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
import time
import pytest
import allure


@allure.title("Mini Project# 9")
@allure.description("mouse interaction")
@pytest.mark.Mini_Project9
def test_mini_project9():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(2)

    atag = driver.find_element(By.ID, 'click')
    atag.click()

    time.sleep(3)
    action = ActionBuilder(driver)
    action.pointer_action.pointer_up(MouseButton.BACK)
    action.perform()
    time.sleep(3)

    driver.quit()

