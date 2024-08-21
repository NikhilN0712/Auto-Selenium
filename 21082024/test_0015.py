from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import allure

@allure.title("Mini Project# 11")
@allure.description("enter the mumbai in make_my_trip dropdown box")
@pytest.mark.Mini_Project11
def test_mini_project11():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")
    time.sleep(2)

    can = driver.find_element(By.XPATH,'//*[@id="SW"]/div[1]/div[2]/div[2]/div/section/span')
    can.click()
    time.sleep(3)

    sel = driver.find_element(By.ID,'fromCity')
    sel.click()

    sed = driver.find_element(By.XPATH,'//*[@id="top-banner"]/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input')
    sed.send_keys("mumbai")

    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(2)

    driver.quit()
