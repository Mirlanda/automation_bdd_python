# Created by Mirlanda at 10/02/2021
Feature: Recover Password

 Scenario: Forget Password
       Given I use the Chrome Browser
       When I open the site
       When I click on Forgot password button
       And A dialog is shown
       And Click in email field
       And I type my email "user@phptravels.com"
       Then click on Reset button
       Then confirm the sending email


