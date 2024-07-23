Feature: Log in page

  Scenario: Navigate to sign in page
    Given Open target.com
    When Click on Sign in button
    When Click on Sign in in navigation panel
    Then Verify log in page

  Scenario: Registered user can sign in
    Given Open target.com
    When Click on Sign in button
    And Click on Sign in in navigation panel
    And Type the email address
    And Type the password
    And Sign in with password
    Then Verify log in was successful