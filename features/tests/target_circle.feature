Feature: Target circle

  Scenario: Check for 10 helpful links
    Given Open target.com
    When Click on Target Circle
    Then Verify all 10 links
