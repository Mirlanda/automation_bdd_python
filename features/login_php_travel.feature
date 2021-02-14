# Created by Mirlanda at 07/02/2021


Feature: Php Travel login

  Scenario Outline: Login to Php travel
    Given I open the Chrome browser
    When I open the php travel site
    And Enter user name "<login>" and password "<password>"
    And Click on login button

    Examples:
      | login                | password  |
      | user@phptravels.com  | demouser  |

