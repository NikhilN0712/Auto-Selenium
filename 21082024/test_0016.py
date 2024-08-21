from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import allure

@allure.title("Mini Project# 12")
@allure.description("enter the mumbai in make_my_trip dropdown box")
@pytest.mark.Mini_Project12
def test_mini_project12():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")
    time.sleep(2)

    sel = driver.find_element(By.XPATH,'//*[@id="content"]/div/a')
    sel.click()

    driver.switch_to.window(driver.window_handles[1])

    tet = driver.find_element(By.TAG_NAME, 'h3')
    assert tet.text == "New Window"


    time.sleep(3)

    driver.quit()


