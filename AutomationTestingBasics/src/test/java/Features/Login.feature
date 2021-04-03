Feature: Login into Application
  Scenario Outline: Positive test validate login
    Given Initialize the browser with chrome
    When Navigate to "qaclickacademy" site
    Then Click on Login link in home page
    When User enters <username> and <password> and logs in
    Then Verify if user is successfully logged in

    Examples:
    | username | password |
    | testtest@gmail.com | 123123 |
    | test123@gmail.com | 21312312 |