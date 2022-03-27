# Regular Expressions

## Use
Regular Expressions are going to be used to find validate a student's email.

## Why use RegEx
When dealing with user's inputs from, for example, forms, they should always be checks to avoid SQL Injection attacks. Regular expressions are a way to make our applications safer to avoid these type of attacks.

## Expression
Currently, the regular expression being used is "up{9}@fe.up.pt$".
- up - Starts with up
- {9} - Any 9 characters
- $ - Ends with "up{9}@fe.up.pt" string

## Tests

When testing this regular expression I used {3} instead of {9} so it would be easier.

Passed (Expected output):
- up22@fe.up.pt - OUTPUT: Invalid Email
- up2222@fe.up.pt - OUTPUT: Invalid Email
- up..22@fe.up.pt - OUTPUT: Invalid Email
- up222fe.up.pt - OUTPUT: Invalid Email
- up222@fe.up.pt - OUTPUT: Valid Email
- ee222@fe.up.pt - OUTPUT: Invalid Emails

Failed (Not valid emails but still passed):
- up.23@fe.up.pt

## Improvements to be made
The current RegEx doesn't check if the nine characters after "up" are numbers ([0-9]).
There are two options:
- Accept the wrongful input the user provided and check if that e-mail exists in the database.
- Find a way to validate if those nine characters are numbers. This can help improving the website's security.

## Info:
- https://www.w3schools.com/python/python_regex.asp