Feature: Sign Up and Confirm Email Functionality

  Background:
    Given the user is on the Sign Up Page

    #passed
  Scenario: Access  SignUp Page
   Then  the user should be redirected to the signup page
#
  Scenario Outline: User fills out all mandatory fields and successfully signs up
    When the user enters "<First Name>" into the First Name field
    And the user enters "<Last Name>" into the Last Name field
    When I enter random email in the email address field
    And the user enters "<Password>" in the password field in signup page
    And the user selects the Terms and Conditions checkbox
    And user clicks on the Sign up button
    Then the user should be redirected to the Confirm Email Page
    Examples:
      | First Name | Last Name | Password |
      | Kashish    | Rajput    | #Test123 |

    #passed
  Scenario Outline: Check error message when mandatory fields are left empty
    When user clicks on the Sign up button
    Then user should able to see "<Firstname error>" error message for firstname
    Then user should able to see "<lastname error>" error message for lastname
    Then user should able to see "<email error>" error message for email
    Then user should able to see "<Password error>" error message for Password
    Then user should able to see "<terms and conditions error>" for terms and conditions
    Examples:
      | Firstname error         | lastname error         | email error        | Password error        | terms and conditions error        |
      | First Name is required! | Last Name is required! | Email is required! | Password is required! | Please accept Terms & Conditions! |
##
#     #passed
  Scenario Outline: Check error message when invalid email format is entered
    When the user enters "<invalidEmail>" in the email address field
    And user clicks on the Sign up button
    Then user should able to see "<email error>" error message for email
    Examples:
      | invalidEmail          | email error            |
      | Kashishrajput         | Invalid Email address! |
      | Kashish rajput@       | Invalid Email address! |
      | Kashish@              | Invalid Email address! |
      | kashishrajput@gmail.  | Invalid Email address! |
      | kashishrajput@gmail.c | Invalid Email address! |

#  #passed
  Scenario Outline: Check error message when email is already in use
    When the user enters "<First Name>" into the First Name field
    And the user enters "<Last Name>" into the Last Name field
    When I enter "<Email Address>" that is already in use in the email address field
    And the user enters "<Password>" in the password field
    And the user selects the Terms and Conditions checkbox
    And user clicks on the Sign up button
    Then I should see an error message that the email is already in use
    Examples:
      | First Name | Last Name | Email Address                   | Password |
      | Kashish    | Rajput    | kashish.rajput@walkingtree.tech | #Test123 |
#
#  #passed
  Scenario Outline: verify signup functionality without accepting the terms and conditions
    When the user enters "<First Name>" into the First Name field
    And the user enters "<Last Name>" into the Last Name field
     When the user enters "<Email Address>" in the email address field
    And the user enters "<Password>" in the password field
    And user clicks on the Sign up button
    Then user should able to see "<terms and conditions error>" for terms and conditions
    Examples:
      | First Name | Last Name | Email Address | Password | terms and conditions error        |
      | Kashish    | Rajput    | kashishrajput@gmail.com | #Test123 | Please accept Terms & Conditions! |

