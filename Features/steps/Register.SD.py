import selenium.webdriver.common.alert
import status
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from behave import *
import time
import selenium.webdriver.common.alert
@given('lauch the browser')
def launch_the_browser(context):
    service = Service(executable_path='C:/Chrome/chromedriver.exe')
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
@when('open the contact form page')
def open_confact_form_page(context):
    context.driver.get('https://automationexercise.com/contact_us')
    time.sleep(3)
@then('verify that logo is present in the page')
def verify_logo(context):
    assert context.driver.find_element(By.XPATH,"//header/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").is_displayed()
@then('enter name "{name}" , email "{email}",subject "{subject}",message "{message}" and upload_file "{upload_file}"')
def enter_details(context,name,email,subject,message,upload_file ):
    context.driver.find_element(By.XPATH,"//input[@data-qa='name']").send_keys(name)
    context.driver.find_element(By.XPATH,"//input[@data-qa='email']").send_keys(email)
    context.driver.find_element(By.XPATH,"//input[@data-qa='subject']").send_keys(subject)
    context.driver.find_element(By.ID,"message").send_keys(message)
    context.driver.find_element(By.XPATH,"//input[@type='file']").send_keys(upload_file)
@then('enter email "{email}"')
def mandatory_fields(context,email):
    context.driver.find_element(By.XPATH,"//input[@data-qa='email']").send_keys(email)
@then('leave name "{name}" , email "{email}",subject "{subject}",message "{message}" and upload_file "{upload_file}" mandatory fields in  blank')
def without_mandatory_fields(context, name, email, subject, message, upload_file):
    context.driver.find_element(By.XPATH, "//input[@data-qa='name']").send_keys(name)
    context.driver.find_element(By.XPATH, "//input[@data-qa='email']").send_keys(email)
    context.driver.find_element(By.XPATH, "//input[@data-qa='subject']").send_keys(subject)
    context.driver.find_element(By.ID, "message").send_keys(message)
    context.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(upload_file)
@then(u'leave name "{name}" , email "{email}",subject "{subject}",message "{message}" and upload_file "{upload_file}" all fields in  empty')
def without_any_field(context,name, email, subject, message, upload_file):
    context.driver.find_element(By.XPATH, "//input[@data-qa='name']").send_keys(name)
    context.driver.find_element(By.XPATH, "//input[@data-qa='email']").send_keys(email)
    context.driver.find_element(By.XPATH, "//input[@data-qa='subject']").send_keys(subject)
    context.driver.find_element(By.ID, "message").send_keys(message)
    context.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(upload_file)
@then('click on submit button')
def submit(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
@then('user receives warning message')
def warning_message(context):
    print(" Received warning message Mandatory field is empty")
    assert context.driver.find_element(By.XPATH,"//div[@class='status alert alert-success']").is_displayed()
    context.driver.quit()
@then('user should navigate to next page and receives confirmation message')
def confirmation_message(context):
    context.driver.switch_to.alert.accept()
    assert context.driver.find_element(By.XPATH,"//div[@class='status alert alert-success']").is_displayed()
@then('close the browser')
def close_browser(context):
    context.driver.close()
