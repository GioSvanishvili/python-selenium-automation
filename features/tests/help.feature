Feature: Tests for Help pages

  Scenario: User can select Help topic Delivery & Pickup
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Delivery & Pickup
    Then Verify help Delivery & Pickup page opened