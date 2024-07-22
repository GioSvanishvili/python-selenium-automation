Feature: Search results page tests

  Scenario: Verify that user can see product names and images
    Given Open target.com
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image
