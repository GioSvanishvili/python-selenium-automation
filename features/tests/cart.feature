Feature: Target cart message


  Scenario: User can see an empty cart message
    Given Open target.com
    When Click on Cart icon
    Then Verify Your cart is empty is shown

  Scenario Outline: User can add items to the cart
    Given Open target.com
    When Search for <item>
    When Click 'Add to cart' on the first item
    And Click 'Add to cart' button on the navigational panel
    And Click 'View cart & check out' button
    Then Verify <cart_amount> item is in cart
    Examples:
    |item          |cart_amount |
    |juice         |1 item      |
    |tea           |1 item      |
    |coffee        |1 item      |