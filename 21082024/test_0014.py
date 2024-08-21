from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
import time
import pytest
import allure


@allure.title("Mini Project# 10")
@allure.description("mouse interaction")
@pytest.mark.Mini_Project10
def test_mini_project10():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(2)

    ele_to_hold = driver.find_element(By.ID, 'draggable')
    ele_to_unhold = driver.find_element(By.ID, 'droppable')
    ele_to_hold.click()

    time.sleep(3)
    action = ActionChains(driver)
    action.click_and_hold(on_element=ele_to_hold).perform()
    #action.drag_and_drop(ele_to_hold,ele_to_unhold)
    time.sleep(5)

    driver.quit()

