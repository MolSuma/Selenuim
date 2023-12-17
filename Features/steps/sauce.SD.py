import selenium.webdriver.common.alert
import status
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
import time
@given(u'launch the chrome browser')
def launch_browser(context):
    service = Service(executable_path='C:/Chrome/chromedriver.exe')
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
@when(u'open the  sauce demo page')
def sauce_demo_page(context):
    context.driver.get('https://www.saucedemo.com/')
    time.sleep(3)
@then(u'verify that logo is present on the page')
def verify_logo(context):
    assert context.driver.find_element(By.XPATH,"//div[contains(text(),'Swag Labs')]").is_displayed()

@then(u'enter admin "<admin>" and password "<password>"')
def enter_details(context):
    context.driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")

@then(u'click on login button')
def login_button(context):
    context.driver.find_element(By.XPATH,"//input[@id='login-button']").click()

@when(u'enter admin "<admin>" and password "<password>"')
def enter_details(context):
    context.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

@then(u'Add one product')
def add_one_product(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(3)


@then(u'Check one item is displayed in shopping cart container')
def check_one_product(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'1')]").is_displayed()
    time.sleep(3)

@when(u'Click on shopping cart container')
def add_to_cart(context):
    context.driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']").click()
    time.sleep(3)

@when(u'close browser')
def close_browser(context):
    context.driver.close()

@when(u'Add three products')
def add_three_products(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()

@then(u'Check  three items are displayed in shopping cart container')
def check_three_products(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'3')]").is_displayed()
    time.sleep(3)

@when(u'Check  three items are displayed in shopping cart container')
def check_three_products(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'3')]").is_displayed()
    time.sleep(3)


@then(u'Add three products')
def add_three_products(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()


@then(u'Click on shopping cart container')
def one_product(context):
    context.driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']").click()
    time.sleep(3)


@then(u'click on checkout button')
def check_out(context):
    context.driver.find_element(By.XPATH,"//button[@id='checkout']").click()


@then(u'navigate to checkout page')
def step_impl(context):
     assert context.driver.find_element(By.XPATH,"//span[contains(text(),'Checkout: Your Information')]").is_displayed()


@then(u'click on twitter link')
def twitter_link(context):
    context.driver.find_element(By.XPATH,"//a[contains(text(),'Twitter')]").click()
    time.sleep(3)
    context.driver.switch_to.default_content()


@then(u'click on facebook link')
def facebook_link(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Facebook')]").click()
    time.sleep(3)
    context.driver.switch_to.default_content()

@then(u'click on linkedIn link')
def linkedIn(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(),'LinkedIn')]").click()
    time.sleep(7)
    context.driver.switch_to.default_content()



