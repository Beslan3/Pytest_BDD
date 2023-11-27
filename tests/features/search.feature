# These are our test cases
# The goal is to have our test cases together with our
# test scripts (python functions) in the same place
# so each scenario (Given, When, Then) from here
# will be mapped each to their own function
# so that the QA can understand better the Engineer's code

# So that way BDD (or Cucumber) frameworks help the QA and
# the Engineer to work closely together
# QA will be saving their test cases under 'features' package
# Engineer will be writing their scripts under
# 'pages', 'step definitions' packages (or folder?)\
# And the execution will happen in the command line


# What we're trying to achieve
Feature: Searching on the web store
  As a customer,
  I want to search a product on the home page
  So I can add the listed product to cart

  # these Gherkin scenarios will be mapped each to
  # their own function
  Scenario: Searching without login
    Given the store home page is displayed
    When the user searches for "dress"
    Then at least one product is listed

