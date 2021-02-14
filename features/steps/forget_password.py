import time

from behave import *
from selenium import webdriver


@given("I use the Chrome Browser")
def step_impl(context):
    context.driver = webdriver.Chrome()


@when("I open the site")
def step_impl(context):
    context.driver.get("https://www.phptravels.net/login")


@when("I click on Forgot password button")
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Forget Password')]").click()
    time.sleep(10)


@when("A dialog is shown")
def step_impl(context):
    pass


@when("Click in email field")
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@placeholder='your@email.com']").click()


@step('I type my email "{email}"')
def step_impl(context, email):
    context.driver.find_element_by_xpath("//input[@placeholder='your@email.com']").send_keys(email)


@then("click on Reset button")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[contains(text(), 'Reset')]").click()
    time.sleep(10)


@then("confirm the sending email")
def step_impl(context):
    element = context.driver.find_element_by_xpath("//form//div[contains(text(),'New Password sent to')]").text
    print(element)
    time.sleep(10)
    assert element == "New Password sent to user@phptravels.com, Kindly check email"
