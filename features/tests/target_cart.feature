Feature: Target cart message


  Scenario: User can see an empty cart message
    Given Open target.com
    When Click on Cart icon
    Then Verify Your cart is empty is shown