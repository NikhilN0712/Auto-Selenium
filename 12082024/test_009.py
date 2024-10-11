from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@allure.title("Mini Project# 5")
@allure.description("add to cart then remove item from cart")
@pytest.mark.Mini_Project5
def test_mini_project5():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")

    clk = driver.find_element(By.NAME,"q")
    clk.send_keys("plant")
    clk.submit()

    ac = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[2]/div/a[2]')
    ac.click()
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    cart = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
    cart.click()
    time.sleep(5)

    re = driver.find_element(By.CSS_SELECTOR,'#container > div > div.z1ALT8 > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div.d\+mEZR.JefwG6 > div._5jL4tC.gRTtwM.f-DWwy > div:nth-child(2)')
    driver.execute_script("arguments[0].scrollIntoView(true);", re)
    re.click()
    time.sleep(5)

    rem1 = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div[3]/div/div[1]')
    rem1.click()
    time.sleep(3)

    driver.quit()