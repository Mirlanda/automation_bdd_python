# Created by Mirlanda at 12/02/2021
Feature: Sign Up - Register new login

  Scenario: Sign Up
    Given I open the browser
    When I open site
    When I click on Sign Up button
    When I fill the First Name "Joas", Last Name "Maria", Mobile Number "992321876", Email "mms@gmail.com", Password "1234567", Confirm password "1234567"
    Then I click on Sign Up button
    Then  I verify email alread existing
