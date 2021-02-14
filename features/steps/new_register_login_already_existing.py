import time

from behave import *
from selenium import webdriver


@given("I open the browser")
def step_impl(context):
    context.driver = webdriver.Chrome()


@when("I open site")
def step_impl(context):
    context.driver.get("https://www.phptravels.net/login")


@when("I click on Sign Up button")
def step_impl(context):
    context.driver.find_element_by_xpath("//form//div//a[contains(text(), 'Sign Up')]").click()


@when('I fill the First Name "{first_name}", Last Name "{last_name}", Mobile Number "{number}", Email "{email}", '
      'Password "{pwd}", Confirm password "{confirm_pwd}"')
def step_impl(context, first_name, last_name, number, email, pwd, confirm_pwd):
    fname = context.driver.find_element_by_css_selector("#headersignupform>div.row>div:nth-child(1)>div>label")
    fname.send_keys(first_name)
    lname = context.driver.find_element_by_css_selector("#headersignupform>div.row>div:nth-child(2)>div>label")
    lname.send_keys(last_name)
    phone = context.driver.find_element_by_css_selector("#headersignupform>div:nth-child(4)>label")
    phone.send_keys(number)
    emailuser = context.driver.find_element_by_css_selector("#headersignupform>div:nth-child(5)>label")
    emailuser.send_keys(email)

    passw = context.driver.find_element_by_css_selector("#headersignupform>div:nth-child(6)>label")
    passw.send_keys(pwd)
    confirm_pass = context.driver.find_element_by_css_selector("#headersignupform>div:nth-child(7)>label")
    confirm_pass.send_keys(confirm_pwd)
    time.sleep(5)


@then("I click on Sign Up button")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Sign Up')]").click()
    time.sleep(10)


@then("I verify email alread existing")
def step_impl(context):
    element = context.driver.find_element_by_xpath("//div[@class='resultsignup']").text
    print(element)
    assert element == "Email Already Exists."
