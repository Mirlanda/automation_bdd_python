from behave import *
from selenium import webdriver


@given('I open the Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open the php travel site')
def step_impl(context):
    context.driver.get("https://www.phptravels.net/login")


@when('Enter user name "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_name("username").send_keys(user)
    context.driver.find_element_by_name("password").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[text()='Login']").click()
