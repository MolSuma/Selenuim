Feature: Contact form registration
    @completed
  Scenario: Verify the logo on the page
    Given lauch the browser
    When open the contact form page
    Then verify that logo is present in the page
    And close the browser
    @completed
  Scenario Outline: Verify with registering all fields
    Given lauch the browser
    When open the contact form page
    Then verify that logo is present in the page
    Then enter name "<name>" , email "<email>",subject "<subject>",message "<message>" and upload_file "<upload_file>"
    Then click on submit button
    Then user should navigate to next page and receives confirmation message
    And close the browser

 Examples:
    |name|  |email|               |subject|   |message|             |upload_file|
    |Suma|  |sumamol27@gmail.com| |Selenium|  |Automating web page| |D:\\Testing\\Demo_file1.txt|
    @completed
  Scenario Outline: Verify with registering only mandatory fields
    Given lauch the browser
    When open the contact form page
    Then verify that logo is present in the page
    Then enter email "<email>"
    Then click on submit button
    Then user should navigate to next page and receives confirmation message
    And close the browser
  Examples:
    |email|
    |sumamol27@gmail.com|
     @completed
   Scenario Outline:Verify  registering without mandatory fields
    Given lauch the browser
    When open the contact form page
    Then verify that logo is present in the page
    Then leave name "<name>" , email "<email>",subject "<subject>",message "<message>" and upload_file "<upload_file>" mandatory fields in  blank
    Then click on submit button
    Then user receives warning message
    And close the browser

 Examples:
    |name|      |email|           |subject|               |message|                     |upload_file|
    |Suma |       |" " |            |Testing |            |Automating websit |          |D:\\Testing\\Demo_file1.txt |
    @completed
  Scenario Outline:Verify  registering with leaving all  fields empty
    Given lauch the browser
    When open the contact form page
    Then verify that logo is present in the page
    Then leave name "<name>" , email "<email>",subject "<subject>",message "<message>" and upload_file "<upload_file>" all fields in  empty
    Then click on submit button
    Then user receives warning message
    And close the browser


 Examples:
    |name|      |email|           |subject|               |message|                     |upload_file|
    |" " |       |" " |            |" " |            |" " |                                |D:\\Testing\\Demo_file1.txt|
