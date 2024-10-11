from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import allure
import time
import pytest

@allure.title("Mini Project #14")
@allure.description("buy the product from online shop")
@pytest.mark.mini_projeck
def test_shopping():
    driver = webdriver.Chrome()
    driver.get("https://practicesoftwaretesting.com/")
    driver.maximize_window()
    time.sleep(2)

#sign in page fill the username and password
    sign_in = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[4]/a')
    sign_in.click()
    time.sleep(2)

    id = driver.find_element(By.ID,"email")
    id.send_keys("nuvibuqo@mailinator.com")
    time.sleep(2)

    pas = driver.find_element(By.XPATH,"//input[@placeholder='Your password']")
    pas.send_keys("NNNn@12344")
    time.sleep(2)

    sub = driver.find_element(By.XPATH,'/html/body/app-root/div/app-login/div/div/div/form/div[3]/input')
    sub.submit()
    time.sleep(2)

    home = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[1]/a')
    home.click()

#shopping for item
    input = driver.find_element(By.XPATH,'//*[@id="filters"]/form[1]/div/select')
    select = Select(input)
    select.select_by_index(1)
    time.sleep(2)

    slider = driver.find_element(By.XPATH,'//*[@id="filters"]/div[1]/ngx-slider/span[6]')
    action = ActionChains(driver)
    action.click_and_hold(slider).move_by_offset(100,0).release().perform()
    time.sleep(2)

    item = driver.find_element(By.XPATH,'/html/body/app-root/div/app-overview/div[3]/div[2]/div[1]/a[9]/div[1]/img')
    item.click()
    time.sleep(2)

    cart = driver.find_element(By.XPATH,"//button[@id='btn-add-to-cart']")
    cart.click()
    time.sleep(2)

    item2 = driver.find_element(By.XPATH, '/html/body/app-root/div/app-detail/div[2]/div/div/a[3]/div[1]/img')
    item2.click()
    time.sleep(2)

    cart = driver.find_element(By.XPATH, "//button[@id='btn-add-to-cart']")
    cart.click()
    time.sleep(10)

#start the billing
    bill = driver.find_element(By.CSS_SELECTOR,'#navbarSupportedContent > ul > li:nth-child(5) > a > fa-icon > svg')
    bill.click()
    time.sleep(2)

    chk = driver.find_element(By.XPATH,'/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/div/button')
    chk.click()
    time.sleep(2)
    chk = driver.find_element(By.XPATH,'/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[2]/app-login/div/div/div/div/button')
    chk.click()
    time.sleep(2)
    chk = driver.find_element(By.XPATH,'/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[3]/app-address/div/div/div/div/button')
    chk.click()
    time.sleep(2)

    chk = driver.find_element(By.ID,"payment-method")
    select = Select(chk)
    select.select_by_index(2)
    time.sleep(2)

    sub = driver.find_element(By.XPATH,"/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-completion-step/app-payment/div/div/div/div/button")
    sub.click()
    time.sleep(2)

    txt = driver.find_element(By.XPATH,"/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-completion-step/app-payment/div/div/div/form/div[2]/div")
    assert txt.text == "Payment was successful"

    allure.attach(driver.get_screenshot_as_png(), name="payment was successful")
    driver.quit()




















