Feature: SignIn Page Navigation and Form Fields

  Background:
    When the user clicks on the SignIn link located on the SignUp page

  #passed
  Scenario: Access SignIn Page from SignUp Page
    Then  the user should be redirected to the SignIn page
#
#  #passed need to check the correct email and password then expectation need to implement
  Scenario Outline: Successful SignIn with Valid Credentials
    When the user enters "<Email>" in the email address field
    And the user enters "<Password>" in the password field
    And the user clicks the SignIn button


    Examples:
      |Email |Password|
      |Murari.Kumar@walkingtree.tech|Mur@ri99340 |
#
##    #passed
  Scenario Outline: verify signIn functionality without email and password
    And the user clicks the SignIn button
    Then user should able to see "<email error>" error message for email
    Then user should able to see "<Password error>" error message for password
    Examples:
      | email error        | Password error        |
      | Email is required! | Password is required! |
#
   #passed
  Scenario Outline: Unsuccessful SignIn with Invalid Credentials
    When the user enters "<Email Address>" in the email address field
    And the user enters "<Password>" in the password field
    And the user clicks the SignIn button
    Then user should able to see "<email error>" error message for email
#    Then user should able to see "<alert>" for password
    Examples:
      | Email Address               | Password | email error            | alert                                                   |
      | kashish.rajput@walkingtree. | 123232  | Invalid Email address! | Password does not match. Please check your credentials. |

#     #passed
  Scenario Outline: Unsuccessful SignIn with Empty email address
    When the user enters "<Password>" in the password field
    And the user clicks the SignIn button
    Then user should able to see "<email error>" error message for email
    Examples:
      |Password|email error|
      |#Kashish@123|Email is required!|
#
#       #passed
  Scenario Outline: Unsuccessful SignIn with Empty Password
    When the user enters "<Email Address>" in the email address field
    And the user clicks the SignIn button
    Then user should able to see "<Password error>" error message for Password
    Examples:
      | Email Address                   | Password error        |
      | kashish.rajput@walkingtree.tech | Password is required! |


