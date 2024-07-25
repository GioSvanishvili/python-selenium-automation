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

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target.com
    When Click on Sign in button
    When Click on Sign in in navigation panel
    Given Store original window
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    When User can close new window and switch back to original