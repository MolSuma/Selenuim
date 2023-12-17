 Feature: Verify the sauce demo functionality
   @completed
  Scenario: Verify logo display
    Given launch the chrome browser
    When open the  sauce demo page
    Then verify that logo is present on the page
    And close browser
     @completed
  Scenario: Verify login with valid credentials
    Given launch the chrome browser
    When open the  sauce demo page
    Then verify that logo is present on the page
    And enter admin "<admin>" and password "<password>"
    And click on login button
    And close browser
     @completed
  Scenario: Verify the add cart functionality with one product.
    Given launch the chrome browser
    When open the  sauce demo page
    Then verify that logo is present on the page
    And enter admin "<admin>" and password "<password>"
    And click on login button
    And Add one product
    And Click on shopping cart container
    And Check one item is displayed in shopping cart container
    And close browser
     @completed
  Scenario: Verify the add cart functionality with three product.
    Given launch the chrome browser
    When open the  sauce demo page
    Then verify that logo is present on the page
    And enter admin "<admin>" and password "<password>"
    And click on login button
    And Add three products
    And Click on shopping cart container
    And Check  three items are displayed in shopping cart container
    And close browser
     @completed
  Scenario: Verify Checkout functionality
    Given launch the chrome browser
    When open the  sauce demo page
    Then verify that logo is present on the page
    And enter admin "<admin>" and password "<password>"
    And click on login button
    And Add three products
    And Click on shopping cart container
    And click on checkout button
    And navigate to checkout page
    And close browser
     @completed
  Scenario: Verify the footer links at the bottom of the page
    Given launch the chrome browser
    When open the  sauce demo page
    Then verify that logo is present on the page
    And enter admin "<admin>" and password "<password>"
    And click on login button
    And click on twitter link
    And click on facebook link
    And click on linkedIn link
    And close browser